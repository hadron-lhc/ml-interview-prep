# Python Interview Module 2 — Strings + Two Pointers + Sliding Window

## Objetivo del módulo

Dominar problemas donde hay que recorrer secuencias eficientemente:

- strings
- listas
- arrays

Y reemplazar brute force O(n²) por soluciones:

- O(n)
- O(n log n)

usando punteros y ventanas móviles.

---

## Qué evalúan en entrevistas

No solo sintaxis.

Evalúan:

- reconocer patrones
- optimizar loops dobles
- manejo de índices
- edge cases
- claridad mental bajo presión

---

# Parte 1 — Strings

## Operaciones clave en Python

```python id="4aqcwn"
s = "hello"

len(s)
s[0]
s[-1]
s[::-1]
s.lower()
s.upper()
s.strip()
s.split()
" ".join(words)
```

---

## Importante

Strings son inmutables.

Esto NO:

```python id="vpk8ig"
s[0] = "H"
```

---

## Patrones típicos con strings

- reverse string
- palindrome
- anagram
- first unique char
- substring search
- frequency count
- compression

---

# Parte 2 — Two Pointers

## Idea central

Usar dos índices que se mueven coordinadamente.

```text id="c1v9hl"
left -> inicio
right -> final
```

---

## Cuándo sospechar Two Pointers

Si aparece:

- sorted array
- palindrome
- pair sum
- reverse in-place
- compare extremos
- shrinking window

---

## Ejemplo clásico: Pair Sum en sorted array

```python id="m5uq6k"
nums = [1,2,4,6,10]
target = 8
```

```python id="ndy4es"
left = 0
right = len(nums)-1
```

- si suma chica → left++
- si suma grande → right--

---

## Complejidad

```text id="1k7dxl"
O(n)
```

vs brute force O(n²)

---

# Parte 3 — Sliding Window

## Idea central

Ventana continua que se expande y contrae.

```text id="x9k6fo"
[left ... right]
```

---

## Cuándo sospechar Sliding Window

Si aparece:

- substring
- subarray
- longest
- shortest
- at most k distinct
- no repeats
- suma de ventana fija
- promedio móvil

---

## Ejemplo fijo tamaño k

Máxima suma de 3 consecutivos:

```python id="b8d2p0"
nums = [1,2,3,4,5]
k = 3
```

Ventanas:

- [1,2,3] = 6
- [2,3,4] = 9
- [3,4,5] = 12

---

## Ejemplo variable

Longest substring without repeating chars.

Expandís right, y si rompe condición:

contraés left.

---

# Mental Models Profesionales

## Si querés comparar extremos

Two pointers.

## Si querés segmento continuo óptimo

Sliding window.

## Si querés conteo dentro de ventana

Window + hashmap.

---

# Errores comunes

## Error 1

Confundir subsequence con substring.

- substring = continuo
- subsequence = puede saltear

---

## Error 2

Off-by-one en índices.

---

## Error 3

No achicar ventana cuando rompe condición.

---

## Error 4

Recalcular suma completa cada vez.

Usar running sum.

---

# Cómo pensar en entrevista

Preguntate:

1. ¿Es secuencia continua?
2. ¿Necesito extremos?
3. ¿Input sorted?
4. ¿Busco longest/shortest?
5. ¿Puedo mover punteros en vez de nested loops?

---

# Complejidades clásicas

- brute force substrings: O(n²) o peor
- two pointers: O(n)
- sliding window: O(n)

(usual amortized)

---

# Frases útiles en entrevista

> Since the array is sorted, I’d use two pointers.

> This is a contiguous segment problem, so sliding window is a strong candidate.

> We can maintain counts incrementally instead of recomputing.

---

# Próximo paso práctico

Problem Set:

1. Valid Palindrome
2. Reverse String
3. Two Sum II (sorted)
4. Best Time to Buy/Sell Stock
5. Longest Substring Without Repeating Characters
6. Minimum Size Subarray Sum
7. Container With Most Water
