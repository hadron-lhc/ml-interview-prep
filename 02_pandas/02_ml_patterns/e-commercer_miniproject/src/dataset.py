import pandas as pd

data = [
    # user, order_id, date, amount, category
    ("u1", 1, "2024-01-01", 100, "electronics"),
    ("u1", 2, "2024-01-03", 50, "books"),
    ("u1", 3, "2024-01-10", 200, "electronics"),
    ("u2", 4, "2024-01-01", 80, "books"),
    ("u2", 5, "2024-01-02", 120, "electronics"),
    ("u2", 6, "2024-01-08", 30, "books"),
    ("u3", 7, "2024-01-01", 200, "electronics"),
    ("u3", 8, "2024-01-04", 150, "electronics"),
    ("u3", 9, "2024-01-06", 50, "books"),
    ("u3", 10, "2024-01-07", 300, "electronics"),
]

df = pd.DataFrame(data, columns=["user", "order_id", "date", "amount", "category"])
df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(["user", "date"])
print(df)
