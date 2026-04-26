# Python Interview Module 1 — Clean Coding + Hashmaps

## Objetivo del módulo

Dominar escritura de código Python:

- clara
- rápida
- robusta
- explicable en entrevista

Y dominar uso profesional de:

```python
dict
set
defaultdict
Counter
```

Porque muchísimos problemas se reducen a estas estructuras.

---

## Qué evalúan en entrevistas con Python

No solo si el código funciona.

Evalúan:

### Correctness

¿Da el output correcto?

### Readability

¿Se entiende rápido?

### Problem Solving

¿Elegiste la estructura adecuada?

### Edge Cases

¿Pensaste vacíos, duplicados, nulls, límites?

### Communication

¿Podés explicar mientras codeás?

### Python Fluency

¿Escribís natural o forzado?

---

## Clean Coding en entrevistas

### Regla 1: Nombres claros

Mal:

```python
d = {}
x = []
a = 0
```

Bien:

```python
counts = {}
result = []
left = 0
```

---

### Regla 2: Una idea por bloque

Evitar mezclar demasiadas responsabilidades dentro del mismo loop.

Mal:

```python
for x in nums:
    if x in seen:
        result.append(x)
    else:
        seen.add(x)
        total += x
```

---

### Regla 3: Early Return

Mejor:

```python
if not nums:
    return []
```

que anidar todo dentro de condiciones.

---

### Regla 4: Claridad > Cleverness

En entrevista:

- No impresionar con rarezas
- Sí escribir código claro

---

### Regla 5: Siempre pensar complejidad

Poder explicar:

```text
Time: O(n)
Space: O(n)
```

---

## Hashmaps: herramienta central

En Python:

```python
dict
```

Mapea:

```text
key -> value
```

Ejemplo:

```python
ages = {
    "ana": 25,
    "juan": 30
}
```

---

## ¿Por qué son tan importantes?

Porque permiten lookup promedio:

```text
O(1)
```

Entonces reemplazan muchos loops dobles O(n²).

---

## Patrones clásicos con dict

### A) Counting Frequency

```python
counts = {}

for num in nums:
    counts[num] = counts.get(num, 0) + 1
```

Sirve para:

- duplicates
- moda
- top frequent
- anagrams

---

### B) Seen Set / Existence Check

```python
seen = set()

for num in nums:
    if num in seen:
        ...
    seen.add(num)
```

Sirve para:

- duplicates
- two sum
- intersections

---

### C) Index Storage

```python
pos = {}

for i, num in enumerate(nums):
    pos[num] = i
```

Sirve para:

- two sum
- nearest duplicate
- previous occurrence

---

### D) Grouping

```python
groups = {}

for word in words:
    key = len(word)
    groups.setdefault(key, []).append(word)
```

Sirve para:

- agrupar strings
- buckets
- categorías

---

## Herramientas profesionales

### defaultdict

```python
from collections import defaultdict

groups = defaultdict(list)
counts = defaultdict(int)
```

Evita checks manuales.

---

### Counter

```python
from collections import Counter

counts = Counter(nums)
```

Ideal para frecuencia.

---

## Problemas típicos de entrevista que usan hashmap

- Two Sum
- Contains Duplicate
- Top K Frequent
- Group Anagrams
- First Unique Character
- Longest Consecutive Sequence
- Subarray Sum = K
- Pair counts
- Join-like merges de listas

---

## Errores comunes

### Error 1

Usar doble loop cuando dict/set resuelve.

```python
for i in nums:
    for j in nums:
```

---

### Error 2

Acceder key inexistente.

```python
counts[x] += 1
```

sin inicializar.

---

### Error 3

Modificar dict mientras iterás.

---

### Error 4

Guardar valor cuando necesitabas índice.

---

## Mental Model Profesional

Cuando veas un problema preguntate:

### ¿Necesito buscar rápido?

Usar:

```python
dict
set
```

### ¿Necesito contar?

Usar:

```python
dict
Counter
```

### ¿Necesito agrupar?

Usar:

```python
defaultdict(list)
```

### ¿Necesito recordar previo?

Usar `dict` guardando índice o posición.

---

## Cómo responder en entrevista

I’d use a hashmap to store frequencies / seen values / prior indices, reducing brute force O(n²) into O(n).

---

## Para roles Data

Hashmaps aparecen en:

- deduplicación
- joins manuales
- parsing JSON
- logs aggregation
- category counts
- feature encoding

---
