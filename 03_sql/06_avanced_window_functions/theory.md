# Módulo 5 — Window Functions (SQL para Entrevistas)

---

## 1. ¿Qué es una Window Function?

Una window function permite:

> Calcular valores sobre un grupo de filas **sin colapsarlas**.

A diferencia de `GROUP BY`, mantiene todas las filas originales.

---

## 2. Estructura base

```sql
SELECT
    ...,
    function(...) OVER (
        PARTITION BY col
        ORDER BY col
    ) AS new_col
FROM table;
```

---

## 3. Mapping con Pandas

| SQL          | Pandas          |
| ------------ | --------------- |
| PARTITION BY | groupby         |
| ORDER BY     | sort_values     |
| LAG / LEAD   | shift           |
| SUM() OVER   | cumsum          |
| ROW_NUMBER   | cumcount / rank |

---

## 4. Tipos de Window Functions

---

### 4.1 Ranking Functions

#### ROW_NUMBER()

```sql
ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY amount DESC)
```

- Sin empates

---

#### RANK()

```sql
RANK() OVER (...)
```

- Empates → saltos (1,1,3)

---

#### DENSE_RANK()

```sql
DENSE_RANK() OVER (...)
```

- Empates sin saltos (1,1,2)

---

---

### 4.2 Offset Functions (CLAVE)

#### LAG()

```sql
LAG(amount) OVER (PARTITION BY user_id ORDER BY order_date)
```

- Valor anterior

---

#### LEAD()

```sql
LEAD(amount) OVER (...)
```

- Valor siguiente

---

### 4.3 Aggregate Windows

#### Running Total

```sql
SUM(amount) OVER (
    PARTITION BY user_id
    ORDER BY order_date
)
```

---

#### Rolling Average

```sql
AVG(amount) OVER (
    PARTITION BY user_id
    ORDER BY order_date
    ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
)
```

---

## 5. Patrones de entrevista

---

### Previous value

```sql
LAG(col) OVER (PARTITION BY user ORDER BY date)
```

---

### Difference

```sql
col - LAG(col) OVER (...)
```

---

### Running total

```sql
SUM(col) OVER (PARTITION BY user ORDER BY date)
```

---

### Top N por grupo

```sql
ROW_NUMBER() OVER (PARTITION BY user ORDER BY metric DESC)
```

---

### First / Last value

```sql
FIRST_VALUE(col) OVER (...)
LAST_VALUE(col) OVER (...)
```

IMPORTANTE:

```sql
LAST_VALUE(col) OVER (
    PARTITION BY user_id
    ORDER BY date
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
)
```

---

## 6. Errores comunes

---

### 1. Olvidar ORDER BY

→ rompe lógica temporal

---

### 2. No usar PARTITION BY

→ mezcla usuarios

---

### 3. Usar GROUP BY en vez de OVER

→ perdés filas

---

### 4. LAST_VALUE mal usado

→ devuelve valor actual si no definís frame

---

## 7. Mental Model

Antes de escribir SQL:

```
1. ¿Es por usuario? → PARTITION BY
2. ¿Es temporal? → ORDER BY
3. ¿Necesito fila anterior? → LAG
4. ¿Es acumulado? → SUM() OVER
5. ¿Es ranking? → ROW_NUMBER / RANK
```

---

## 8. Regla de oro

> Si en Pandas usarías `groupby + shift`, en SQL usás:

```sql
LAG() OVER (PARTITION BY ... ORDER BY ...)
```

---

## 9. Resumen rápido

| Problema        | Solución SQL      |
| --------------- | ----------------- |
| valor anterior  | LAG               |
| valor siguiente | LEAD              |
| acumulado       | SUM OVER          |
| ranking         | ROW_NUMBER / RANK |
| rolling         | ROWS BETWEEN      |

---

## Objetivo

Dominar window functions = resolver la mayoría de problemas SQL en entrevistas.

---
