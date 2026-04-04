## JOINs

Qué evaluan con joins:

- Modelo relacional
- Cómo pensar datos distribuidos
- Lógica de matching
- Edge cases (NULLs, duplicates)

---

### 1 -- Teoría

Un JOIN combina filas de dos tablas basadas en una condición lógica:

Piensalo como:
"¿Para cada fila de A, qué filas de B matchean?"

Forma general:

```SQL
SELECT columns
FROM table_A
JOIN table_B
ON A.id = B.id
```

La diferencia entre los tipos de Joins es qué se hace con las filas que no matchean

---

#### Tipos importantes de JOiN

- INNER JOIN -> intersección
- LEFT JOIN -> todo izquierda + matches
- RIGHT JOIN -> todo derecha + matches
- FULL JOIN -> izquierda, derecha o null

Los críticos:

INNER
LEFT

---

#### Tablas de ejemplo

employees:

| id  | name | department_id |
| --- | ---- | ------------- |
| 1   | Ana  | 10            |
| 2   | Luis | 20            |
| 2   | Juan | NULL          |

departments:

| id  | department  |
| --- | ----------- |
| 10  | Engineering |
| 20  | HR          |
| 30  | Sales       |

---

### 2 -- INNER JOIN

Devuelve solo matches

```SQL
SELECT e.name, d.department
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
```

Resultado:

| name | department  |
| ---- | ----------- |
| Ana  | Engineering |
| Luis | HR          |

Juan desaparece porque:
NULL no matchea.

Regla mental:
INNER JOIN = intersection

Pattern interview mental:
"Solo quiero filas válidas en ambas tablas"

---

### 3 -- LEFT JOIN

Toda la tabla izquierda no se filtra

```SQL
SELECT e.name, d.department
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.id
```

Resultado:

| name | departemnt  |
| ---- | ----------- |
| Ana  | Engineering |
| Luis | HR          |
| Juan | NULL        |

Regla mental:
LEFT JOIN = preserve left table

Interview mental shortcut:
LEFT JOIN = "no pierdas data"

---

#### Diferencia INNER vs LEFT

INNER:
Filtra implícitamente.

LEFT:
No filtra.

Ejemplo clásico:
"Find employees without department"

Solución:

```SQL
SELECT e.name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.id
WHERE d.id IS NULL
```

---

### 3 -- Patrones muy usados

Estos aparecen constantemente:

Pattern 1 (Lookup pattern):

```SQL
JOIN dimension table
```

Pattern 2 (Find missing relationships):

```SQL
LEFT JOIN
WHERE right.id IS NULL
```

Pattern 3 (Aggregation after join):

```SQL
JOIN
GROUP BY

```

---

#### Tablas para ejemplos

employees:

| id  | name  | department  | salary |
| --- | ----- | ----------- | ------ |
| 1   | Ana   | Engineering | 90000  |
| 2   | Luis  | Engineering | 85000  |
| 3   | Carla | HR          | 70000  |
| 4   | Pedro | HR          | 72000  |
| 5   | Sofia | Sales       | 65000  |

departments:

| department  | manager |
| ----------- | ------- |
| Engineering | Alice   |
| HR          | Bob     |
| Sales       | Charlie |

---

### 4 -- Ejemplos

Ejemplo 1:

Get employee + manager

```SQL
SELECT e.name, e.salary, d.manager
FROM employees e
JOIN departmens d
ON e.department = d.department
```

Ejemplo 2:

Average salary per manager

```SQL
SELECT
    d.manager,
    AVG(e.salary)
FROM employees e
JOIN departments d
ON e.department = d.department
GROUP BY d.manager
```

---

### 5 — Patrones mentales profesionales

Siempre pensar:

1. Qué tabla es base?
2. Qué tabla agrega info?
3. Qué key conecta?
4. Puede haber duplicates?
5. Puede haber NULLs?

Mental checklist entrevista:

BASE table
JOIN table
KEY
TYPE of JOIN
EDGE CASES

Ejemplo thinking correcto:

"Quiero salarios → base employees"

"Quiero manager → join departments"

Key:

department

JOIN:

INNER (si asumimos integridad)

LEFT (si queremos robustez)

---

### 6 — Errores típicos de candidatos

##### Error 1

Olvidar ON:

```SQL
FROM A, B
```

→ Cartesian product disaster.

##### Error 2

Join wrong column.

##### Error 3

Filtering after LEFT JOIN:

Esto rompe LEFT JOIN:

```SQL
LEFT JOIN B
WHERE B.column = 'X'
```

Convierte en INNER.

Forma correcta:

```SQL
LEFT JOIN B
ON A.id = B.id
AND B.column = 'X'
```
