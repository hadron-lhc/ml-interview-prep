## Fast and Slow Ponters

La idea:

Mover dos punteros a distintas velocidades o con distintos roles

---

### Cuando se usa

Generalmente cuando hay:

```text
Linked lists
Arrays
Cycle detection
Palindromes
Middle elements
```

---

### Tipos de Fast/Slow Patterns

#### 1 - Clycle detection (el clasico)

Ejemplo:

slow avanza 1
fast avanza 2

Si hay ciclo se van a encontrar.

##### Template

```python
slow = head
fast = head

while fast and fast.next:

    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        cycle
```

#### 2 - Find middle

Si:

slow avanza 1
fast avanza 2

Cuando fast termina:

slow está en el medio.

##### Template

```python
slow = head
fast = head

while fast and fast.next:

    slow = slow.next
    fast = fast.next.next

return slow
```

#### 3 - Opposite pointers (array version)

```python
left = 0
right = len(arr)-1
```

Ejemplo:
Palindrome:

```python
while left < right:

    if arr[left] != arr[right]:

        return False

    left += 1

    right -= 1
```

---

#### Problemas mas tipicos

- Detect cycle in linked list
- Find middle of linked list
- Palindrome linked list
- Happy number (muy famoso)
- Remove nth from end
