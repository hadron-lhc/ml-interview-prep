## Pandas

### Las 5 operaciones core de Pandas

#### 1 Filtering

```python
df[df["age"] > 30]
```

#### 2 Groupby

```python
df.groupby("department")["salary"].mean()
```

#### 3 Aggregation

```python
df.agg({
  "salary": "mean",
  "age": "max",
})
```

#### 4 Joins

```python
df.merge(other, on="id")
```

#### 5 Missing data

```python
df.fillna()
df.dropna()
```

---

### De SQL a Pandas

La mayoria de los ejercicios de entrevistas son traducir una query a pandas

#### Ejemplo

SQL:

```SQL
SELECT department, AVG(salary)
FROM employees
GROUP BY department
```

Pandas:

```python
df.groupby("department")["salary"].mean()
```
