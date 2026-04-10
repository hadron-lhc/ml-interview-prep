# Pandas ML Patterns

## 1 — CUMULATIVE / PREFIX PATTERN

### Idea

Acumulás información en el tiempo.

### Operaciones clave

```python
cumsum()
cummax()
cummin()
cumcount()
```

### Ejemplo

```python
df["running_total"] = df.groupby["user"]("amount").cumsum()
```

### Uso real ML

Features tipo:

```text
total gastado hasta ahora
número de eventos hasta ahora
máximo histórico
```

### Insight

Esto es:

prefix sum aplicado a data.

---

## 2 — SHIFT / LAG PATTERN (CRÍTICO)

### Idea

Comparar con el pasado.

### Operación clave

```python
shift()
```

#### Ejemplo

```python
df["prev_amount"] = df.groupby["user"]("amount").shift(1)
```

#### Derivados importantes

```python
df["diff"] = df["amount"] - df["prev_amount"]

df["pct_change"] = df["amount"] / df["prev_amount"]
```

#### Uso real ML

Features:

```text
crecimiento
cambio
variación temporal
tendencias
```

### SQL equivalente

```SQL
LAG(amount)
```

### Insight

Esto es:

comparación temporal → clave en ML

---

## 3 — ROLLING WINDOW PATTERN

### Idea

Mirar una ventana de tamaño fijo.

### Operación

```python
rolling(window=3)
```

### Ejemplo

```python
df["rolling_mean"] = df.groupby["user"]("amount").rolling(3).mean().reset_index(0, drop=True)
```

### Uso real ML

Features:

```text
promedio últimos 7 días
suma últimos N eventos
volatilidad
```

### Insight

Esto es:

sliding window en data real

---

## 4 — GROUPBY + TRANSFORM (MUY IMPORTANTE)

### Idea

Aplicar una operación por grupo, pero mantener el shape.

### Diferencia clave

```python
groupby().agg() → reduce filas
groupby().transform() → mantiene filas
```

### Ejemplo

```python
df["user_avg"] = df.groupby["user"]("amount").transform("mean")
```

### Uso real

```text
normalizar por usuario
comparar contra promedio del grupo
```

### Ejemplo entrevista

```python
df["above_avg"] = df["amount"] > df["user_avg"]
```

### SQL equivalente

```SQL
AVG() OVER(PARTITION BY user)
```

---

## 5 — RANKING PATTERN

### Idea

Ordenar dentro de grupos.

### Operación

```python
rank()
```

### Ejemplo

```python
df["rank"] = df.groupby["user"]("amount").rank(ascending=False)
```

### Uso real

```text
top cliente
top compra
orden dentro del grupo
```

### Insight

Esto es:

window functions en Pandas.

---

## 6 — FILTERING WITH GROUPS

### Idea

Filtrar basado en propiedades del grupo.

### Ejemplo

```python
df.groupby("user").filter(lambda x: len(x) > 2)
```

### Uso real

```text
usuarios con suficientes datos
grupos relevantes
```

---

## 7 — MERGE / JOIN PATTERN

### Idea

Combinar datasets.

### Operación

```python
pd.merge()
```

### Ejemplo

```python
df = df.merge(users, on="user_id", how="left")
```

### Uso real

```text
features externas
lookup tables
enrichment
```

Insight

Esto es SQL JOIN en Pandas.

---

## 8 — APPLY VS VECTORIZATION (CRÍTICO)

### Idea

Evitar loops.

## X Malo

```python
df["new"] = df["amount"].apply(lambda x: x*2)
```

## ✔ Mejor

```python
df["new"] = df["amount"]\* 2
```

## Uso real

Performance.

## Regla de oro

Si podés evitar apply, hacelo.

---

## 9 — MISSING DATA PATTERN

### Operaciones

```python
isna()
fillna()
dropna()
```

### Ejemplo

```python
df["amount"] = df["amount"].fillna(0)
```

## Uso real ML

Data cleaning.

---

## 10 — FEATURE ENGINEERING PATTERN (LO MÁS IMPORTANTE)

### Idea

Combinar todo lo anterior.

### Ejemplo real

```python
df = df.sort_values(["user","date"])

df["prev"] = df.groupby["user"]("amount").shift(1)

df["diff"] = df["amount"] - df["prev"]

df["rolling_mean"] = df.groupby["user"]("amount").rolling(3).mean().reset_index(0, drop=True)

df["cumsum"] = df.groupby["user"]("amount").cumsum()

```

### Resultado

Dataset listo para ML.

---

## 11 — ORDEN (CRÍTICO)

#### Siempre

```python
df = df.sort_values(["group","time"])
```

#### Antes de

shift
rolling
cumsum

---

## 12 — MAPEO MENTAL (MUY IMPORTANTE)

| Concepto       | Python | Pandas  | SQL          |
| -------------- | ------ | ------- | ------------ |
| Prefix sum     | loop   | cumsum  | SUM OVER     |
| LAG            | manual | shift   | LAG          |
| Sliding window | loop   | rolling | window frame |
| Hashmap        | dict   | groupby | GROUP BY     |

---

### 13 — LO QUE BUSCAN EN ENTREVISTAS

##### No buscan

memorizar funciones.

##### Buscan

✔ reconocer patrón
✔ elegir herramienta correcta
✔ escribir código limpio
✔ evitar loops
