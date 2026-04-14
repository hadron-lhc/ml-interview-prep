# 1. Qué es “estado” vs “evento”

## Evento

Algo que ocurre en un punto específico:

- una compra
- un login
- superar un threshold
- cancelar suscripción

#### es instantáneo

## Estado

Una condición que se mantiene en el tiempo:

- usuario activo/inactivo
- en churn / no churn
- en una racha / no racha

#### es persistente

🔥 Insight clave

```text
Los problemas difíciles NO son de eventos.
Son de transiciones de estado.
```

---

# 2. Tipos de problemas que aparecen en entrevistas

## Tipo 1 — Event Detection

Detectar cuándo pasa algo:

```text
primer compra > 100
primer login
primer churn
```

## Tipo 2 — State Tracking

Seguir un estado en el tiempo:

```text
usuario activo/inactivo
acumulando gasto
en streak
```

## Tipo 3 — State Transition

Detectar cambios:

```text
activo → inactivo
no churn → churn
no premium → premium
```

---

# 3. Los 4 patrones fundamentales

## Patrón 1 — Previous State

```python
prev = groupby().shift(1)
```

base de TODO

## Patrón 2 — Event Detection

Detectar primer evento:

```python
cond = df["amount"] > 100

event = cond & (~cond.groupby(df["user_id"]).shift(1).fillna(False))
```

Traducción

```text
cond es True
Y antes era False
```

“esto acaba de pasar”

## Patrón 3 — Running State

```python
state = groupby().cumsum()
```

o

```python
state = groupby().cummax()
```

### Cuándo usar cada uno

| Función | Significado          |
| ------- | -------------------- |
| cumsum  | contar eventos       |
| cummax  | “ya pasó alguna vez” |

## Patrón 4 — Reset con grupos dinámicos

Para streaks:

```python
groups = (~cond).cumsum()
streak = cond.groupby(groups).cumsum()
```

### Traducción

```text
cada vez que cond es False → nuevo grupo
```

esto crea segmentos dinámicos

---

# 4. Patrones compuestos

### A. “Primera vez que pasa algo”

```python
cond & (~cond.shift())
```

### B. “Desde que pasó algo”

```python
cond.cumsum() > 0
```

### C. “Después de X días sin evento”

```python
diff_dates >= threshold
```

### D. “Cambios de estado”

```python
state != state.shift()
```

---

# 5. Errores clásicos

### 1. Confundir acumulado con secuencia

```python
cumsum() != streak
```

### 2. No usar shift

sin shift no hay tiempo

### 3. No agrupar correctamente

mezclar usuarios = FAIL automático

### 4. No manejar NaNs

primera fila SIEMPRE especial

---

# 6. Mental Model

Cuando veas un problema:

### Paso 1

¿Es evento o estado?

### Paso 2

¿Necesito el pasado?

sí → shift

### Paso 3

¿Es acumulado o transición?

| Caso       | Herramienta       |
| ---------- | ----------------- |
| acumulado  | cumsum            |
| transición | shift + condición |

### Paso 4

¿Hay resets?

sí → grupos dinámicos (cumsum sobre negación)

---

# 7. Ejemplo completo mental

Problema:

```text
detectar primera vez que un usuario entra en churn
```

### Paso 1

```python
inactive = days_since_last_order >= 30
```

### Paso 2 (evento)

```python
first_churn = inactive & (~inactive.shift())
```
