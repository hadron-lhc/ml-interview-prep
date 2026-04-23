/*

Ejercicio 1 (Easy)

Consecutive Login Days

  Usando tabla "logins"
  Queremos detectar streaks de días consecutivos por usuario.

Output esperado:
| user_id | streak_start | streak_end | days |

Para user 1:
  - Jan1 → Jan3 = 3
  - Jan8 → Jan9 = 2

Para user 2:
  - Jan1 = 1
  - Jan3 → Jan5 = 3

Para user 3:
  - Jan10 = 1

*/

/*

WITH base AS (
  SELECT
        DISTINCT user_id,
        login_date,
        ROW_NUMBER() OVER (
          PARTITION BY user_id
          ORDER BY login_date
        ) rn
  FROM logins
),
grouped_logins AS (
  SELECT *,
         DATE(login_date, '-' || rn || ' day') AS grp
  FROM base
)
SELECT
      user_id,
      MIN(login_date) AS streak_start,
      MAX(login_date) AS streak_end,
      COUNT(*) AS days
FROM grouped_logins
GROUP BY user_id, grp;

*/

---------------------------------------------------------------------------

/*
Ejercicio 2 (Easy+)

Days Since Previous Login

Usando logins, devolver:

| user_id | login_date | prev_login | days_since_prev |

Con NULL en primer login.

Acá quiero que uses:

  - LAG()
  - diferencia de fechas en SQLite

*/

/*
WITH base AS (
  SELECT
    user_id,
    login_date,
    LAG(login_date) OVER (
      PARTITION BY user_id
      ORDER BY login_date
    ) AS prev_login
  FROM logins
)
SELECT
  user_id,
  login_date,
  prev_login,
  CASE
    WHEN prev_login IS NULL THEN NULL
    ELSE JULIANDAY(login_date) - JULIANDAY(prev_login)
  END AS days_since_prev
FROM base
ORDER BY user_id, login_date;
*/

------------------------------------------------------------------------

/*
Ejercicio 3 (Medium)

Longest Login Streak Per User

Usando logins, devolver:
| user_id | longest_streak |

Para datos actuales:
    user 1 → 3
    user 2 → 3
    user 3 → 1

*Quiero que lo resuelvas reutilizando islands.*
*/

/*
WITH base AS (
  SELECT
    DISTINCT user_id,
    login_date,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY login_date
    ) rn
  FROM logins
),
grouped_logins AS (
  SELECT *,
         DATE(login_date, '-' || rn || ' day') AS grp
  FROM base
),
streaks AS (
  SELECT
    user_id,
    grp,
    COUNT(*) AS streak
  FROM grouped_logins
  GROUP BY user_id, grp
)
SELECT
  user_id,
  MAX(streak) AS longest_streak
FROM streaks
GROUP BY user_id
ORDER BY user_id;
*/

-----------------------------------------------------------

/*
Ejercicio 4 — Sessionization

Tabla:

events(user_id, event_time)

Nueva sesión si pasaron más de 30 minutos desde el evento anterior.

Queremos output:

| user_id | session_id | session_start | session_end | events_in_session |
*/

WITH base AS (
  SELECT
    user_id,
    event_time,
    LAG(event_time) OVER (
      PARTITION BY user_id
      ORDER BY event_time
    ) AS prev_event
  FROM events
),

gaps AS (
  SELECT *,
    (JULIANDAY(event_time) - JULIANDAY(prev_event)) * 24 * 60 AS diff_minutes
  FROM base
),

flags AS (
  SELECT *,
    CASE
      WHEN prev_event IS NULL THEN 1
      WHEN diff_minutes > 30 THEN 1
      ELSE 0
    END AS new_session
  FROM gaps
),

sessions AS (
  SELECT *,
    SUM(new_session) OVER (
      PARTITION BY user_id
      ORDER BY event_time
      ROWS UNBOUNDED PRECEDING
    ) AS session_id
  FROM flags
)

SELECT
  user_id,
  session_id,
  MIN(event_time) AS session_start,
  MAX(event_time) AS session_end,
  COUNT(*) AS events_in_session
FROM sessions
GROUP BY user_id, session_id
ORDER BY user_id, session_id;
