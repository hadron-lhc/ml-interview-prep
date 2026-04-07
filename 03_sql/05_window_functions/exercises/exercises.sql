/*
EXERCISE 1 (warmup)

Rankear empleados por salario global.

Output esperado:
| name | salary | rank |

Usar:
ROW_NUMBER
*/

SELECT *

FROM (

  SELECT
  name,
  salary,

  ROW_NUMBER() OVER (
    ORDER BY salary DESC
  ) AS rm

  FROM employees

) t;

/*
EXERCISE 2

Rankear empleados por salario dentro del departamento.

Output:
| name | department | salary | rank |

Usar:
PARTITION BY
 */

SELECT *

FROM(

  SELECT
    e.name AS employee_name,
    d.name AS department_name,
    e.salary,

    ROW_NUMBER() OVER (
      PARTITION BY d.name
      ORDER BY salary DESC
    ) AS rn

  FROM
    employees e

  LEFT JOIN
    departments d

  ON e.department_id = d.id

) t;

/*
EXERCISE 3

Mostrar:
empleado
salario
promedio del departamento

Output:
| name | salary | dept_avg |

Usar:
AVG OVER
 */


SELECT *

FROM (

  SELECT
    e.name,
    e.salary,

    AVG(e.salary) OVER (
      PARTITION BY d.id
    ) AS dept_avg

  FROM employees e

  LEFT JOIN departments d
  ON e.department_id = d.id

) t;


/*
EXERCISE 4 (interview clásico)

Mostrar empleados que ganan más que el promedio de su departamento.

Hint:
subquery + window.
 */


SELECT *

FROM (

  SELECT
    e.name,
    e.salary,

    AVG(e.salary) OVER (
      PARTITION BY d.id
    ) AS dept_avg

  FROM employees e
  LEFT JOIN departments d
  ON e.department_id = d.id

) t

WHERE salary > dept_avg;


/*
EXERCISE 5

Top empleado mejor pago por departamento.

Expected:
| department | name | salary |

Hint:
ROW_NUMBER = 1
 */


SELECT *

FROM (

  SELECT
    d.name,
    e.name,
    e.salary,

    ROW_NUMBER() OVER (
      PARTITION BY d.id
      ORDER BY e.salary DESC
    ) AS rn

  FROM employees e
  LEFT JOIN departments d

  ON e.department_id = d.id

) t

WHERE rn = 1;



/*
EXERCISE 6

Top 2 salarios por departamento.

Hint:
ROW_NUMBER <= 2
 */

SELECT *

FROM (

  SELECT
    e.name,
    d.name,
    e.salary,

    ROW_NUMBER() OVER (
      PARTITION BY d.id
      ORDER BY e.salary DESC
    ) AS rn

    FROM
      employees e

    LEFT JOIN
      departments d

    ON
      e.department_id = d.id

) t

WHERE rn <= 2;


/*
 EXERCISE 7 — Ranking de órdenes

Rankear todas las órdenes por monto (de mayor a menor).

Output:
| order_id | amount | rank |

Usar:
ROW_NUMBER()

Opcional (bonus):
hacer también RANK y DENSE_RANK para ver la diferencia.
 */

SELECT
  id,
  amount,

  ROW_NUMBER() OVER (
    ORDER BY amount DESC
  ) AS rn,

  RANK() OVER (
    ORDER BY amount DESC
  ) AS ranking,

  DENSE_RANK() OVER (
    ORDER BY amount DESC
  ) AS dense_ranking

  FROM orders;



/*
 EXERCISE 8 — Total vendido por empleado (muy importante)

Para cada orden mostrar:
order_id
employee_name
amount
total_vendido_por_ese_employee

Output:
| order_id | employee | amount | employee_total |

Hint:
SUM() OVER(PARTITION BY ...)

Este es muy común en entrevistas de Data Engineer.
 */


SELECT
  o.id AS order_id,
  e.name AS employee,
  o.amount,

  SUM(o.amount) OVER (
    PARTITION BY e.id
  )

FROM orders o
JOIN employees e
ON o.employee_id = e.id


/*
EXERCISE 9 — Previous order (LAG)

Para cada orden mostrar:

order_id
amount
previous_order_amount

Output:

| order_id | amount | prev_amount |

Hint:

LAG()

ORDER BY order_date.
 */

SELECT
  id AS order_id,
  amount,

  LAG(amount) OVER (
    ORDER BY order_date
  ) AS prev_amount

FROM
  orders;


/*
 EXERCISE 10 — Next order (LEAD)

Igual que el anterior pero:
next_order_amount

Output:
| order_id | amount | next_amount |

Hint:
LEAD()
 */


SELECT
  id AS order_id,
  amount,

  LEAD(amount) OVER (
    ORDER BY order_date
  ) AS next_amount

FROM
  orders;


/*
 EXERCISE 11 — Running total global (muy importante)

Para cada orden mostrar:
order_id
order_date
amount
running_total

Output:
| order | date | amount | running_total |

Hint:
SUM OVER + ORDER BY order_date

Esto aparece mucho en:
fintech
analytics
ML feature pipelines
 */

SELECT
  id AS order_id,
  order_date,
  amount,

  SUM(amount) OVER (
    ORDER BY order_date
  ) AS running_total

FROM
  orders;

/*
 EXERCISE 12 — Running total por employee

Igual que el anterior pero:
reinicia por empleado.

Output:
| order | employee | amount | running_total |

Hint:
PARTITION BY employee_id
ORDER BY order_date

Este es un patrón muy importante.
 */

SELECT
  o.id AS order_id,
  e.name AS employee,
  o.amount,

  SUM(amount) OVER (
    PARTITION BY o.employee_id
    ORDER BY o.order_date
  ) AS running_total

FROM
  orders o

JOIN
  employees e

ON
  o.employee_id = e.id;


/*
 EXERCISE 13 — Ranking de empleados por ventas (Amazon style)

Mostrar:
employee_name
total_sales
sales_rank

Output:
| employee | total_sales | rank |

Hint:
Primero sumar ventas por employee.
Después rankear.

Necesitarás:
SUM
subquery
RANK()

Este es nivel entrevista real.
 */


WITH SalesSummary AS (
  SELECT
    e.name AS employee,
    (SELECT SUM(amount) FROM orders o WHERE o.employee_id = e.id) AS total_sales
  FROM employees e
)
SELECT
  employee,
  total_sales,
  RANK() OVER (ORDER BY total_sales DESC) AS rank
FROM SalesSummary;


/*
 EXERCISE 14 — Second highest salary (clásico eterno)

Encontrar el segundo salario más alto.

Output:
| name | salary |

Hay varias formas.

La forma profesional usa:
DENSE_RANK()
 */

WITH RankingSalarial AS(
  SELECT
    name,
    salary,
    DENSE_RANK() OVER (
      ORDER BY SALARY DESC
    ) AS dr
  FROM employees
)

SELECT
  name,
  salary

FROM
  RankingSalarial

WHERE dr = 2;

/*
 EXERCISE 15 — Orden más cara por cliente (patrón FAANG)

Para cada customer mostrar:
customer_name
order_id
amount

Pero solo su orden más cara.

Output:
| customer | order | amount |

Hint:
ROW_NUMBER()
PARTITION BY customer_id
ORDER BY amount DESC

Este aparece muchísimo.
 */


WITH OrdersPerClient AS (

  SELECT
    c.name AS customer_name,
    o.id AS order_id,
    o.amount AS amount,

    ROW_NUMBER() OVER (
      PARTITION BY o.customer_id
      ORDER BY o.amount DESC
    ) AS rank_orders

  FROM customers c
  JOIN orders o ON c.id = o.customer_id

)

SELECT
  customer_name,
  order_id,
  amount

FROM OrdersPerClient

WHERE rank_orders = 1;



