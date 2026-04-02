## Top K pattern

---

Este pattern aparece cuando el problema realmente dice:

"No necesito todo ordenado... Solo los primeros K"

### Ejemplos reales

- Top 10 features mas importantes
- Top 20 palabras TF-IDF
- Top 5 recomendaciones
- Top anomalias
- Top scores modelo

### Problema base

```python
words = ["a","b","a","c","b","a"]
```

frecuencia:
a -> 3
b -> 2
c -> 1

queremos top 2:
a,b

#### Solucion intuitiva pero no optima

```python
sorted(count.items(), key=lambda x:x[1], reverse=True)
```

- Estamos ordenando cosas que no queremos
- Mientras mas grande es el array peor es

#### Sorting

"Ordena toda la lista y luego toma K"

#### Heap

"Solo mantiene los K mejores mientras recorre"

### Proceso (con heap)

7 → [7]

2 → [2,7]

9 → [2,7,9]

1 → discard

5 → replace 2

3 → discard

#### Resultado

[5,7,9]

---

## Libreria

```python
import heapq
```

### Operaciones importantes

Insertar:

```python
heapq.heappush(heap, x)
```

Sacar menor:

```python
heapq.heappop(heap)
```

Push + pop:

```python
heapq.heappushpop(heap, x)
```

### Ejemplo simple

```python
import heapq

heap = []

heapq.heappush(heap,5)
heapq.heappush(heap,2)
heapq.heappush(heap,9)

print(heap)
```

output: [2,5,9]

(siempre el menor primero)

### Implementacion conceptual

```python
heap = []

for word,freq in count.items():

    if len(heap) < k:
        push

    else:
        if freq > heap[0][0]:
            replace
```
