from dataset import df_1
import pandas as pd

"""
Objetivo

Crear:
   - days_since_last_order

Output esperado
user_id | order_date | days_since_last_order
-------------------------------------------
1       | 2023-01-01 | NaN
1       | 2023-01-10 | 9
1       | 2023-02-01 | 22
2       | 2023-01-05 | NaN
2       | 2023-03-01 | 55
"""


def featuring(df):
    df = df.copy()
    # Ordenar por fecha
    df["order_date"] = pd.to_datetime(df["order_date"])
    df = df.sort_values(["user_id", "order_date"]).reset_index(drop=True)

    # Agregar nuevo feature
    df["last_order"] = df.groupby("user_id")["order_date"].shift(1)
    df["days_since_last_order"] = (df["order_date"] - df["last_order"]).dt.days
    df.drop(columns=["last_order"], inplace=True)
    return df


def main():
    df = df_1
    df_featured = featuring(df)
    print(df_featured)


if __name__ == "__main__":
    main()
