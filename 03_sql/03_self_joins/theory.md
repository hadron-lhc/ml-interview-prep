## SELF JOINs

Un SELF JOIN es:

Un JOIN donde la tabla se une consigo misma.

##### Ejemplo conceptual

employees:

| id  | name  | manager_id |
| --- | ----- | ---------- |
| 1   | Ana   | NULL       |
| 2   | Luis  | 1          |
| 3   | Carla | 1          |

Pregunta:
Quién es el manager de Luis?

Respuesta:
Buscar employee_id = manager_id.

---

### Mental model

Pensar:

- La tabla representa:
  una entidad

- Pero también representa:
  la relación

- employees es:
  personas
  y jerarquía

- Entonces hacemos:
  employees (employee role)
  employees (manager role)

---

### Regla fundamental

Siempre usar alias claros:

```SQL
employees e
employees m
```

Nunca:

```SQL
employees a
employees b
```

---
