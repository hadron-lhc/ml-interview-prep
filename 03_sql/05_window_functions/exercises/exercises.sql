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
    promedio


)


/*
EXERCISE 5

Top empleado mejor pago por departamento.

Expected:
| department | name | salary |

Hint:
ROW_NUMBER = 1
 */


/*
EXERCISE 6

Top 2 salarios por departamento.

Hint:
ROW_NUMBER <= 2
 */



