# Gaps & Islands

Este tema mezcla:

- Lógica temporal
- window functions
- modelado mental
- capacidad analítica real
- SQL elegante

---

## 1. Qué es Gaps and Islands?

Es una familia de problemas donde tenes eventos ordenados en el tiempo y queres detectar:

### Islands = bloques consecutivos

#### Ejemplo

Usuario compra en:

| user | date       |
| ---- | ---------- |
| A    | 2024-01-01 |
| A    | 2024-01-02 |
| A    | 2024-01-03 |
| A    | 2024-01-07 |
| A    | 2024-01-08 |

Aca hay dos islands:

- Isla 1 -> 1,2,333
- Isla 2 -> 7,8

Gaps (huecos entre eventos):

- gap entre 3 y 7 = 4 dias

### Traduccion real de negocio

Esto aparece como:

- rachas de uso consecutivo
- dias activos seguidos
- sesiones web
- tiempo entre compras
- churn temporal
- reactivaciones
- fraude por actividad anormal
- pacientes sin visitas
- sensores que dejan de reportar

---

## 2. Por qué es importante en entrevistas?

Porque testea varias capas:

### Nivel basico

Saber usar LAG()

### Nivel intermedio

Saber detectar consecutividad

### Nivel fuerte

Poder agrupar secuencias automaticamente

### Nivel profesional

Saber convertir negocio ambiguo en logica temporal

---

## 3. Cómo detectarlo mentalmente

Cuando leas un problema, si aparece algo como:

- consecutive
- streak
- in a row
- days since last
- inactive for x days
- returned after gap
- sessions
- continuous activity
- sequence
- next event
- previous event

---

## 4. Los 3 patrones universales

### Patrón A - LAG + Difference

Usas el evento anterior para medir distancia.

```SQL
LAG(event_date)
```

Luego:

```SQL
DATEDIFF(day, prev_date, event_date)
```

Sirve para:

- dias desde ultima compra
- detectar breaks
- churn
- sessions

### Ejemplo

| date |
| ---- |
| Jan1 |
| Jan2 |
| Jan5 |

| date | prev | gap  |
| ---- | ---- | ---- |
| Jan1 | null | null |
| Jan2 | Jan1 | 1    |
| Jan5 | Jan2 | 3    |

### Patrón B - Row Number Trick

El más famoso para detectar consecutivos

Idea:
Si las fechas son consecutivas:

```SQL
date - row_number()
```

queda constante.

#### Ejemplo

| date | rn  | date - rn |
| ---- | --- | --------- |
| Jan1 | 1   | Dec31     |
| Jan2 | 2   | Dec31     |
| Jan3 | 3   | Dec31     |
| Jan7 | 4   | Jan3      |
| Jan8 | 5   | Jan3      |

Jan1, Jan2, Jan3 comparten grupo
Jan7, Jan8 tambien

Esto crea islands automaticamente.

### Patrón C - Cumulative Grouping

Detectas cuando empieza nuevo bloque

```SQL
CASE WHEN gap > 1 THEN 1 ELSE 0 END
```

Luego:

```SQL
SUM(flag) OVER (...)
```

Eso genera IDs de grupo.

### Ejemplo

| date | gap  | new_group | grp_id |
| ---- | ---- | --------- | ------ |
| Jan1 | null | 1         | 1      |
| Jan2 | 1    | 0         | 1      |
| Jan3 | 1    | 0         | 1      |
| Jan7 | 4    | 1         | 2      |
| Jan8 | 1    | 0         | 2      |

---

## 5. Técnicas SQL típicas

### Técnica 1 - Longest Consecutive Streak

Pregunta clasica:
Cual fue la mayor racha de dias activos por usuario?

### Esquema

```SQL
WITH x AS (
  SELECT
    user_id,
    activity_date,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY activity_date
    ) rn
  FROM activity
),
y AS (
  SELECT *,
         activity_date - rn * INTERVAL '1 day' AS grp
  FROM x
)
SELECT user_id,
       MIN(activity_date),
       MAX(activity_date),
       COUNT(*) streak
FROM y
GROUP BY user_id, grp;
```

Usa el patrón B. Visto anteriormente, para generar las islas

### Técnica 2 - Time Since Previous Event

```SQL
LAG(date)
DATEDIFF(...)
```

### Técnica 3 - Sessionization

Nueva sesión si gap > 30 min.

```sql
CASE WHEN diff_minutes > 30 THEN 1 ELSE 0 END
```

Después cumulative sum.

---

## 6. Errores comunes

### Error 1: No deduplicar fechas

Si usuario hizo 3 eventos el mismo día:

| user | date |
| ---- | ---- |
| A    | Jan1 |
| A    | Jan1 |
| A    | Jan2 |

Para streak diario quizá necesitas:

```SQL
SELECT DISTINCT user_id, date
```

### Error 2: No particionar por usuario

```SQL
LAG(date) OVER (ORDER BY date)
```

mezcla usuarios.

Debe ser:

```SQL
OVER (PARTITION BY user_id ORDER BY date)
```

### Error 3: No ordenar correctamente timespatamps

Sessions dependen de orden exacto

### Error 4: Confundir ROWS vs RANGE

Ya lo vimos antes.
Acá casi siempre querés ROWS o row_number ordenado.

### Error 5: Definir mal consecutivo

¿Consecutivo significa:

- calendar days?
- business days?
- active days?
- every purchase within 7 days?

Esto en entrevista se pregunta.

---

## 8. Cómo reconocerlo en entrevistas

Cuando te digan:

#### “Find users with 3 consecutive login days”

Pensá:

- islands
- row_number trick

#### “Users inactive for 30+ days then returned”

Pensá:

- LAG + gap

#### “Split events into sessions”

Pensá:

- lag timestamp
- cumulative grouping

#### “Longest streak”

Pensá:

- islands + count

---

## 9. Comparación con Pandas (importantísima para vos)

### SQL

```SQL
LAG(date)
```

### Pandas

```python
df["prev"] = df.groupby["user"]("date").shift()
```

### SQL cumulative groups

```SQL
SUM(flag) OVER (...)
```

### Pandas

```python
df["grp"] = flag.cumsum()
```

### SQL row_number trick

```SQL
ROW_NUMBER()
```

### Pandas

```python
cumcount()
```

---

## 10. Framework Mental Profesional

Cuando veas problema temporal:

### Paso 1

¿Qué define continuidad?

- 1 día
- 30 min
- misma categoría
- no gap > X

### Paso 2

¿Qué define corte?

### Paso 3

¿Necesito previous row?

→ LAG

### Paso 4

¿Necesito grupos?

→ cumulative sum o row_number trick

### Paso 5

¿Necesito resumen final?

→ GROUP BY group_id
