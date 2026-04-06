# WINDOW FUNCTIONS

---

# 1 — El problema que Window Functions resuelven

Primero el problema.

Supongamos:

employees:

| name  | department | salary |
| ----- | ---------- | ------ |
| Ana   | Eng        | 95     |
| Luis  | Eng        | 87     |
| Carla | Eng        | 91     |
| Pedro | HR         | 72     |
| Sofia | HR         | 68     |

Pregunta:

**¿Cuál es el empleado mejor pago por departamento?**

Con GROUP BY:

```sql
SELECT department, MAX(salary)
FROM employees
GROUP BY department;
```

Resultado:

| department | max_salary |
| ---------- | ---------- |
| Eng        | 95         |
| HR         | 72         |

Problema:

Perdimos:

nombre del empleado.

GROUP BY **colapsa filas**.

Window Functions permiten:

**hacer agregaciones SIN colapsar filas.**

Esa es la idea central.

---

# 2 — Definición formal

Window Function:

Una función que:

**opera sobre un conjunto de filas relacionadas
pero sin agruparlas en una sola fila.**

Diferencia clave:

GROUP BY:

reduce filas.

WINDOW:

mantiene filas.

---

# 3 — Sintaxis básica

Forma general:

```sql
function() OVER(
PARTITION BY column
ORDER BY column
)
```

Ejemplo:

```sql
AVG(salary) OVER(PARTITION BY department)
```

Esto significa:

Calcular el promedio salarial dentro del departamento,
pero mantener cada fila.

---

# 4 — Primer ejemplo real

Query:

```sql
SELECT
name,
department,
salary,

AVG(salary) OVER(PARTITION BY department) AS dept_avg

FROM employees;
```

Resultado:

| name  | dept | salary | dept_avg |
| ----- | ---- | ------ | -------- |
| Ana   | Eng  | 95     | 91       |
| Luis  | Eng  | 87     | 91       |
| Carla | Eng  | 91     | 91       |
| Pedro | HR   | 72     | 70       |
| Sofia | HR   | 68     | 70       |

Observación importante:

No agrupamos.

Solo agregamos información.

Esto es clave en ML:

Feature engineering.

---

# 5 — PARTITION BY (concepto clave)

PARTITION BY es:

GROUP BY para window functions.

Pero:

NO colapsa filas.

Ejemplo:

```sql
PARTITION BY department
```

Significa:

Dentro de cada department
calcular la función.

Mental model:

Dividir la tabla en mini tablas.

Pero sin separarlas físicamente.

---

# 6 — ORDER BY dentro de OVER

Ejemplo:

```sql
ROW_NUMBER() OVER(
PARTITION BY department
ORDER BY salary DESC
)
```

Esto significa:

Dentro del department:

ordenar por salary.

Después numerar.

Resultado:

| name  | dept | salary | row |
| ----- | ---- | ------ | --- |
| Ana   | Eng  | 95     | 1   |
| Carla | Eng  | 91     | 2   |
| Luis  | Eng  | 87     | 3   |

Esto es **ranking por grupo.**

Pregunta clásica de entrevistas.

---

# 7 — Window Functions más importantes

Las más importantes:

ROW_NUMBER()  
RANK()  
DENSE_RANK()  
AVG() OVER  
SUM() OVER  
LAG()  
LEAD()

---

# 8 — ROW_NUMBER

Ejemplo:

```sql
SELECT

name,
department,
salary,

ROW_NUMBER() OVER(
PARTITION BY department
ORDER BY salary DESC
) AS row_num

FROM employees;
```

Resultado:

| name  | dept | salary | row_num |
| ----- | ---- | ------ | ------- |
| Ana   | Eng  | 95     | 1       |
| Carla | Eng  | 91     | 2       |
| Luis  | Eng  | 87     | 3       |

Uso típico:

Top N per group.

---

# 9 — RANK vs DENSE_RANK

Dataset:

| name  | salary |
| ----- | ------ |
| Ana   | 95     |
| Luis  | 90     |
| Carla | 90     |
| Pedro | 80     |

RANK:

| name  | rank |
| ----- | ---- |
| Ana   | 1    |
| Luis  | 2    |
| Carla | 2    |
| Pedro | 4    |

Salta números.

DENSE_RANK:

| name  | rank |
| ----- | ---- |
| Ana   | 1    |
| Luis  | 2    |
| Carla | 2    |
| Pedro | 3    |

No salta.

Pregunta MUY común en entrevistas.

---

# 10 — Comparación

ROW_NUMBER:

Siempre único.

RANK:

Empates comparten rank.

DENSE_RANK:

Empates comparten pero sin saltos.

---

# 11 — Top employee per department (patrón clásico)

Solución profesional:

```sql
SELECT *

FROM(

SELECT
name,
department,
salary,

ROW_NUMBER() OVER(
PARTITION BY department
ORDER BY salary DESC
) AS r

FROM employees

) t

WHERE r=1;
```

Esto aparece constantemente en entrevistas.

---

# 12 — SUM OVER (totales por grupo)

Ejemplo:

```sql
SUM(salary) OVER(
PARTITION BY department
)
```

Esto da:

Total payroll por dept,
pero sin agrupar.

Ejemplo:

| name  | dept | salary | total |
| ----- | ---- | ------ | ----- |
| Ana   | Eng  | 95     | 273   |
| Luis  | Eng  | 87     | 273   |
| Carla | Eng  | 91     | 273   |

---

# 13 — ORDER BY sin PARTITION

Ejemplo:

```sql
ROW_NUMBER() OVER(
ORDER BY salary DESC
)
```

Ranking global.

---

# 14 — LAG

LAG permite:

Comparar con fila anterior.

Ejemplo:

```sql
LAG(salary) OVER(
ORDER BY salary
)
```

Resultado:

| salary | prev |
| ------ | ---- |
| 68     | NULL |
| 72     | 68   |
| 87     | 72   |

Uso típico:

Time series  
Trend analysis  
Feature differences

---

# 15 — LEAD

Lo mismo pero siguiente fila:

```sql
LEAD(salary) OVER(
ORDER BY salary
)
```

---

# 16 — Window Frame (concepto avanzado)

Ejemplo:

```sql
SUM(salary) OVER(
ORDER BY salary
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
```

Esto genera:

Running total.

Lo veremos más adelante con ejercicios.

---

# 17 — Diferencia real

GROUP BY:

Reduce:

10 filas → 3 filas.

WINDOW:

Mantiene:

10 filas → 10 filas.

Pero agrega métricas.

---

# 18 — Error conceptual común

Esto está mal:

```sql
WHERE ROW_NUMBER() OVER(...)
```

Porque:

WHERE ocurre antes.

Solución:

Subquery o CTE.

---

# 19 — Patrón profesional real

Siempre:

```sql
SELECT *
FROM(

window logic

) t

WHERE filter;
```

Esto es estándar.

---

# 20 — Patrones que aparecen en entrevistas

Top employee per department  
Second highest salary  
Salary ranking  
Compare employee vs dept avg  
Employees above average  
Running totals  
Salary percentiles

---

# 21 — Ejemplo importante

Employees above department average:

```sql
SELECT *

FROM(

SELECT

name,
salary,
department,

AVG(salary) OVER(
PARTITION BY department
) AS dept_avg

FROM employees

) t

WHERE salary > dept_avg;
```

Esto aparece MUCHO.

---

# 22 — Mental model correcto

Pensar:

Window Functions =

**features sobre filas**

Esto es exactamente:

Feature engineering.

Ejemplo ML:

user_avg_spend  
transaction_rank  
previous_purchase  
rolling_average

Todo esto usa window functions.

---

# 23 — Regla de oro

Si necesitas:

Aggregar sin perder filas → WINDOW

Si necesitas:

Reducir dataset → GROUP BY

---

# 24 — Interview insight importante

Preguntas típicas:

Top 3 per department  
Second highest salary  
Employees above avg  
Rank products per category

Todas:

Window functions.

---

# 25 — Qué diferencia SQL básico de SQL bueno

SQL básico:

JOIN  
GROUP BY

SQL bueno:

WINDOW  
CTE  
Subqueries

---

# 26 — Regla práctica

Si ves:

Top per group → ROW_NUMBER

Si ves:

Compare to group → AVG OVER

Si ves:

Previous row → LAG

---

# 27 — Resumen mental

Las 3 más importantes:

ROW_NUMBER → ranking  
AVG OVER → comparación  
LAG → comparación temporal

Si dominás esas 3:

Estás listo para muchas entrevistas.

---
