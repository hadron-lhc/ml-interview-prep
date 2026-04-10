/*
PROBLEM 1 — Top performer por ventas

Mostrar:
department_name
employee_name
total_sales

Pero solo el empleado que más vendió en cada departamento.

Output:
| department | employee | total_sales |

Hints:
Step mental model:
  1 sumar ventas por employee
  2 traer department
  3 rankear dentro del department
  4 quedarte con rank 1
*/

WITH SalesPerEmployee AS (

  SELECT
    d.name AS department,
    e.name AS employee,
    SUM(o.amount) AS total_sales

  FROM orders o

  JOIN employees e
    ON o.employee_id = e.id

  JOIN departments d
    ON e.department_id = d.id

  GROUP BY
    d.name,
    e.name
),

Ranked AS (

  SELECT *,
    ROW_NUMBER() OVER (
      PARTITION BY department
      ORDER BY total_sales DESC
    ) AS ranking

  FROM SalesPerEmployee

)

SELECT
  department,
  employee,
  total_sales

FROM Ranked

WHERE ranking = 1;


/*
PROBLEM 2 — Employees above department sales average

Mostrar empleados cuyo total de ventas es mayor que el promedio de ventas de su departamento.

Output:
| employee | department | total_sales | dept_avg |

Mental steps:
1 total sales per employee
2 avg sales per department
3 comparar

Skills:

GROUP
WINDOW
FILTER
*/

WITH SalesPerEmployee AS (

  SELECT
    e.id,
    e.name AS employee,
    d.id AS dept_id,
    d.name AS department,

    SUM(o.amount) AS total_sales,

  FROM orders o

  JOIN employees e
    ON o.employee_id = e.id

  JOIN departments d
    ON e.department_id = d.id

  GROUP BY
    e.id,
    e.name,
    d.id,
    d.name
),

WithAvg AS(

  SELECT *,

  AVG(total_sales) OVER(
  PARTITION BY dept_id
  ) AS dept_avg

  FROM SalesPerEmployee

)

SELECT *

FROM WithAvg

WHERE total_sales > dept_avg;

/*
PROBLEM 3 — Customer lifetime value ranking

Mostrar:
  - customer
  - total_spent
  - customer_rank

Rankear clientes por cuánto gastaron.

Output:
| customer | total_spent | rank |

Bonus:
  Mostrar también:
    percent_rank()

Skills:
  * GROUP
  * RANK
  * DENSE_RANK
*/


WITH SpentPerCustomer AS (

  SELECT
    c.id,
    c.name AS customer,

    SUM(o.amount) AS total_spent,

  FROM orders o

  JOIN customers c
    ON o.customer_id = c.id

  GROUP BY c.id, c.name
)

SELECT
  customer,
  total_spent,

  DENSE_RANK() OVER(
    ORDER BY total_spent DESC
  ) AS ranking,

  PERCENT_RANK() OVER(
    ORDER BY total_spent DESC
  ) AS percent_ranking

  FROM SpentPerCustomer;


/*
PROBLEM 4 — First order vs last order (temporal)

Para cada customer mostrar:
  - customer
  - first_order_amount
  - last_order_amount
  - difference

Output:
| customer | first | last | diff |

Hints:
  * FIRST_VALUE
  * LAST_VALUE
  * window ORDER BY date.

Skills:
Temporal windows.
*/

WITH OrdersPerCustomer AS (

  SELECT
    c.name AS customer,
    o.order_date,
    o.amount,

    ROW_NUMBER() OVER (
      PARTITION BY c.id
      ORDER BY o.order_date ASC
    ) AS oldest_rank,

    ROW_NUMBER() OVER (
      PARTITION BY c.id
      ORDER BY o.order_date DESC
    ) AS recent_rank


  FROM orders o

  JOIN customers c
  ON o.customer_id = c.id

)

SELECT
  customer,

  MAX(CASE WHEN oldest_rank = 1 THEN amount END) AS oldest_amount,

  MAX(CASE WHEN recent_rank = 1 THEN amount END) AS recent_amount,

  MAX(CASE WHEN recent_rank = 1 THEN amount END)
  -
  MAX(CASE WHEN oldest_rank = 1 THEN amount END) AS difference

FROM OrdersPerCustomer

GROUP BY customer;


/*
PROBLEM 5 — Sales trend detection (muy real ML feature)

Para cada orden mostrar:
  - order_id
  - employee
  - amount
  - previous_amount
  - difference

Output:
| order | employee | amount | prev | diff |

Hint:
LAG
amount - LAG(amount)

Esto es literalmente:
Feature engineering.

*/

WITH AmountsPerOrder AS (

SELECT
  o.id AS order_id,
  e.name AS employee,
  o.amount AS amount,

  LAG(o.amount) OVER (
    ORDER BY order_date
  ) AS last_amount

FROM orders o
JOIN employees e
  ON o.employee_id = e.id

)

SELECT
  order_id,
  employee,
  amount,
  last_amount,
  amount - last_amount

FROM AmountsPerOrder;

  
