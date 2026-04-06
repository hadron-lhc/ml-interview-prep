## Multi Joins

Cuando hay 3 tablas:

Nunca pensar:
"join todo"

Pensar:
chain relationships

---

#### Ejemplo

```text
employees → departments → locations
```

No:

```text
employees → locations directamente.
```

---

### Professional mental model

Pensar como grafo:

```text
employees -- department --> departments -- department --> locations
```

Cada JOIN:
expande contexto.

---

#### Regla profesional

Siempre preguntarse:
What connects these tables?

Nunca:
"qué columnas tienen el mismo nombre".

---

#### Multi JOIN pattern general

```SQL
FROM base_table

JOIN table_1
ON relationship

JOIN table_2
ON relationship
```

Siempre:
JOIN en orden lógico.
