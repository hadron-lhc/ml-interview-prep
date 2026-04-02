## Hashmaps (dict)

Lo importante es detectar patrones, tarea recurrente de "Contar cuántas veces aparece algo"

### Palabras claves

- frequency
- most common
- duplicates
- unique
- first unique
- top K
- histrogram

### Patron base

```python
counts = {}

for item in data:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
```

Esto es el counting pattern básico.

#### Complejidad

- Tiempo: O(n)
- Espacio: O(k) (elementos únicos)

### Version mas limpia (get)

```python
counts = {}

for item in data:
    counts[item] = counts.get(item,0) + 1
```
