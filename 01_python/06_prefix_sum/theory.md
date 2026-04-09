# Prefix Sum Patterns

## 1 -- La intuición

En vez de recalcular sumas muchas veces, precomputamos sumas acumuladas.

Ejemplo:

Tenemos:

```python
arr = [2,4,1,6,3]
```

Queremos:

sum entre índice 1 y 3:

```python
4 + 1 + 6 = 11
```

Forma naive:

```python
sum(arr[l:r+1])
```

Complejidad:
O(n)

Si hacemos muchas queries:
O(n²)

---

### La idea prefix sum

Construimos:

```python
prefix = [2,6,7,13,16]
```

Donde:

```python
prefix[i] = suma desde 0 hasta i
```

Entonces:

```python
sum(l,r) = prefix[r] - prefix[l-1]
```

Ejemplo:

```python
sum(1,3)

prefix[3] - prefix[0]

13 - 2 = 11

```

Ahora:

O(1)

Esto es el patrón.

---

## 2 -- La implementación base

Forma estándar:

```python
def build_prefix(arr):

    prefix = [0]*len(arr)

    prefix[0] = arr[0]

    for i in range(1,len(arr)):

        prefix[i] = prefix[i-1] + arr[i]

    return prefix
```

Complejidad:

Build -> O(n)
Query -> O(1)

Esto es:

Trade computation for speed

---

## 3 — Variante profesional

Agregar un 0 inicial:

```python
arr = [2,4,1,6,3]

prefix = [0,2,6,7,13,16]
```

Construcción:

```python
prefix = [0]

for num in arr:
prefix.append(prefix[-1] + num)
```

Ahora:

Formula:

```python
sum(l,r) = prefix[r+1] - prefix[l]
```

Esto evita:

edge cases.

Los engineers prefieren esto.

---

## 4 — El patrón mental real

##### Prefix sum sirve cuando ves

- many range queries
- subarrays
- cumulative values
- running metrics

##### Keywords

"sum between"
"range sum"
"subarray sum"
"cumulative"
"running total"

Si ves esto:

Pensar prefix sum automáticamente.

---

## 5 — Ejemplo real tipo entrevista

##### Problem

Cuántos subarrays suman K.

##### Ejemplo

```python
[1,2,3]
k = 3
```

###### Subarrays

```text
[1,2]
[3]
```

Respuesta:
2

Naive:
O(n²)

Prefix:
O(n)

---

## 6 — La extensión importante

HashMap + prefix sum

##### Idea

Si:

```python
prefix[j] - prefix[i] = k
```

##### Entonces

```python
prefix[i] = prefix[j] - k
```

##### Entonces guardamos

frecuencias de prefix sums.

##### Implementación

```python
def subarray_sum(nums,k):

    prefix = 0

    seen = {0:1}

    count = 0

    for num in nums:

        prefix += num

        if prefix-k in seen:
            count += seen[prefix-k]

        seen[prefix] = seen.get(prefix,0)+1

    return count
```

Este problema aparece mucho.

---

## 7 — Donde aparece esto en ML

Esto conecta con:

### Feature engineering

##### Ejemplo

rolling averages.

```python
df["running_sales"] = df["sales"].cumsum()
```

Eso es:

prefix sum.

---

### También

Time series features:

- rolling mean
- cumulative metrics
- moving windows

Ejemplo:

```python
df["7day_sum"]
df["cumulative_users"]
df["running_revenue"]
```

Todos usan esta idea.

---

### También conecta con SQL

Ejemplo:

```SQL
SUM(amount) OVER(
ORDER BY date
)
```

Eso es prefix sum.

---

### También aparece en

- Gradient accumulation
- Loss tracking
- Metric smoothing

---

## 8 — Diferencia con sliding window

Muchos los confunden.

##### Sliding window

ventana dinámica.

##### Prefix

acumulado global.

##### Sliding

```python
sum last k
```

##### Prefix

```python
sum any range
```

---

## 9 — Errores típicos

##### Error 1

Olvidar el 0 inicial.

##### Error 2

Index off by one.

##### Error 3

No usar hashmap cuando hace falta.

##### Error 4

Recalcular sumas.

Si ves:

```python
sum(arr[i:j])
```

Muchas veces:

Probablemente hay optimización.

---

## 10 — Variantes del patrón

Este pattern tiene extensiones:

- Prefix min
- Prefix max
- Prefix count
- Prefix frequency

Ejemplo:

```python
prefix_min[i]
prefix_max[i]
```

También:

Difference arrays (muy importante).

---

## 11 — Nivel entrevista

Si dominás prefix sum podés resolver:

Muchos medium LeetCode.

##### Muy común en

- Data roles
- ML interviews
- Quant interviews

---

## 12 — Ejercicios que vamos a hacer

Vamos a hacer progresivo:

##### Level 1

running sum

##### Level 2

range queries

##### Level 3

subarray sum

##### Level 4

prefix hashmap

##### Level 5

ML style cumulative features

---

## 13 — El mindset importante

No memorices código.

Memorizá esto:

Cuando veas:

Range queries
Cumulative values
Repeated sums

Pensar:

¿puedo precomputar esto?
