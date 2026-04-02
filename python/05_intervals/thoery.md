## Intervals

Qué es un interval:

```text
[star, end]
```

Ejemplo:

```text
[1,3]
[2,6]
[8,10]
[15,18]
```

---

### Problema central de intervals

Detectar

```text
[1,3]
[2,6]
```

Esto es overlap, porque:

```text
2 <= 3
```

#### Regla universal de overla

Dos intervals son overlap si:

```text
start2 <= end1
```

(asumiendo sorted)

Visualización:

```text
[1|--|3]
   [2|----|6]
```

---

### Regla de merge

Si overlap:
Nuevo interval

```python
start = min(start1,start2)

end = max(end1,end2)
```

Ejemplo:

```text
[1,3]
[2,6]
```

Merge:

```text
[1,6]
```

---

### Insight

El 90% de los problemas comienzan así, con sorted

```python
intervals.sort(key=lambda x: x[0])
```

---

### Template universal

```python
intervals.sort()

result = []

current = intervals[0]

for interval in intervals[1:]:

    if overlap:

        merge

    else:

        result.append(current)

        current = interval

result.append(current)
```
