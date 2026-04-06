## Advanced GROUP BY

### Error conceptual común

Muchos piensan:

- WHERE filtra filas
- GROUP BY agrupa
- HAVING filtra grupos

Pero el orden real es:

```text
FROM
JOIN
WHERE
GROUP BY
HAVING
SELECT
ORDER
```

---

### Ejemplo mental

employees:

| name  | dept | salary |
| ----- | ---- | ------ |
| Ana   | Eng  | 90     |
| Luis  | Eng  | 85     |
| Carla | HR   | 70     |

Si haces:

```SQL
WHERE salary > 80
```

Primero filtra:

Ana
Luis

Después agrupa.

Si haces:

```SQL
HAVING AVG(salary) > 80
```

Primero agrupa.
Después filtra grupos.
