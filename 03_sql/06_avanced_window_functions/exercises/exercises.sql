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


-- ================================
-- PROBLEMA 3 — Running Revenue Share
-- ================================
-- pct_of_user_total_so_far


-- ================================
-- PROBLEMA 4 — Top 2 Orders per User
-- ================================


-- ================================
-- PROBLEMA 5 — Streak Length (HARD)
-- ================================


-- ================================
-- PROBLEMA 6 — Sessionization (HARD)
-- ================================


-- ================================
-- PROBLEMA 7 — Reactivated Users (HARD)
-- ================================
