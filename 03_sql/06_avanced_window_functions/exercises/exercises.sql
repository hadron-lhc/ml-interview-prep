-- ================================
-- PROBLEMA 1 — Days Since Last Order
-- ================================
-- Calcular days_since_last_order

SELECT
    user_id,
    order_date,
    amount,
    CAST(
        julianday(order_date) -
        julianday(LAG(order_date) OVER (PARTITION BY user_id ORDER BY order_date))
    AS INTEGER) AS days_since_last_order
FROM orders;


-- ================================
-- PROBLEMA 2 — First Order After Signup
-- ================================
-- Marcar is_first_order_after_signup


WITH base AS(
  SELECT
    o.user_id,
    o.order_date,
    o.amount,
    u.signup_date,
    ROW_NUMBER() OVER (
      PARTITION BY o.user_id
      ORDER BY o.order_date
    ) AS rn
  FROM orders o
  JOIN users u
    ON o.user_id = u.user_id
  WHERE o.order_date > u.signup_date
)

SELECT
  user_id,
  order_date,
  amount,
  CASE WHEN rn = 1 THEN 1 ELSE 0 END AS is_first_order_after_signup
FROM base
ORDER BY user_id, order_date;

-- ================================
-- PROBLEMA 3 — Running Revenue Share
-- ================================
-- pct_of_user_total_so_far

-- orders(user_id, order_date, amount)
WITH base AS (
  SELECT
    user_id,
    order_date,
    amount,
    SUM(amount) OVER (
      PARTITION BY user_id
      ORDER BY order_date
    ) AS acum,
    SUM(amount) OVER (
      PARTITION BY user_id
    ) AS user_total
  FROM orders
)
SELECT
  user_id,
  order_date,
  amount,
  acum,
  user_total,
  ROUND(acum * 100.0 / user_total, 2) AS pct_of_user_total_so_far
FROM base;


-- ================================
-- PROBLEMA 4 — Top 2 Orders per User
-- ================================

-- users(user_id, signup_date)
-- orders(user_id, order_date, amount)
WITH orders_per_user AS(
  SELECT
    u.user_id,
    o.amount,
    ROW_NUMBER() OVER (
      PARTITION BY u.user_id
      ORDER BY o.amount DESC
    ) AS rn
  FROM users u
  LEFT JOIN orders o
    ON u.user_id = o.user_id
)

SELECT
  user_id,
  amount,
  rn
FROM orders_per_user
WHERE rn <= 2;


-- ================================
-- PROBLEMA 5 — Streak Length (HARD)
-- ================================

-- orders(user_id, order_date, amount)
WITH base AS (
    SELECT
        user_id,
        order_date,
        amount,
        LAG(amount) OVER (
            PARTITION BY user_id
            ORDER BY order_date
        ) AS prev_amount
    FROM orders
),

flags AS (
    SELECT
        *,
        CASE
            WHEN prev_amount IS NULL THEN 0
            WHEN amount > prev_amount THEN 1
            ELSE 0
        END AS inc
    FROM base
),

grp AS (
    SELECT
        *,
        SUM(CASE WHEN inc = 0 THEN 1 ELSE 0 END)
        OVER (
            PARTITION BY user_id
            ORDER BY order_date
            ROWS UNBOUNDED PRECEDING
        ) AS grp_id
    FROM flags
)

SELECT
    user_id,
    order_date,
    amount,
    prev_amount,
    inc,
    CASE
        WHEN inc = 0 THEN 0
        ELSE ROW_NUMBER() OVER (
            PARTITION BY user_id, grp_id
            ORDER BY order_date
        ) - 1
    END AS streak_length
FROM grp
ORDER BY user_id, order_date;

-- ================================
-- PROBLEMA 6 — Sessionization (HARD)
-- ================================


-- ================================
-- PROBLEMA 7 — Reactivated Users (HARD)
-- ================================
