## Sliding Window

### Idea fundamental

Muchos problemas dicen algo como:

- Encontrar el mejor subarray
- Substring mas largo
- Promedio movil
- Ventana de tamaño K
- Secuencia valida mas larga
- Segmento continuo

Eso suele significar Sliding Window

---

### Problema base clasico

Supongamos:

```python
nums = [2,1,5,1,3,2]
k = 3
```

Encontrar:
Subarray de tramaño 3 con suma maxima

Subarray posibles:

```text
[2,1,5] = 8
[1,5,1] = 7
[5,1,3] = 9
[1,3,2] = 6
```

Resultado: 9

### Solucion ineficiente

```python
max_sum = 0

for i in range(len(nums)-k+1):
    window_sum = sum(nums[i:i+k])
    max_sum = max(max_sum,window_sum)
```

Complejidad: O(k\*n)

### Solucion sliding window

Por desplazamiento del subarray

```python
window_sum = sum(nums[:k])

max_sum = window_sum

for i in range(k,len(nums)):
    window_sum += nums[i]
    window_sum -= nums[i-k]
    max_sum = max(max_sum,window_sum)
```

Complejidad: O(n)

---

### Tipos de sliding window

#### Fixed window (tamaño fijo)

Ventana de tamaño K

```text
add right
remove left
```

#### Dynamic window (tamaño variable)

Ej: Substring mas largo sin repetir caracteres

```text
expand right
shrink left until valid
```

---

### Template fixed window

```python
build first window

for remaining elements:

    add right

    remove left

    update answer
```

### Template dynamic window

```python
left = 0

for right in range():

    add element

    while invalid:

        remove left
        left +=1

    update answer
```
