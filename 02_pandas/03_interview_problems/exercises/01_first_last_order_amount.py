from dataset import df_1
import pandas as pd

"""
Objetivo

Para cada fila, agregar:

    - first_order_amount
    - last_order_amount

Output esperado
user_id | order_date | amount | first_order_amount | last_order_amount
----------------------------------------------------------------------
1       | ...        | 100    | 100                | 200
1       | ...        | 150    | 100                | 200
...
"""


def featuring(df):
    df = df.copy()

    # Ordenar por fecha
    df["date"] = pd.to_datetime(df["order_date"])
    df = df.sort_values(["user_id", "order_date"]).reset_index(drop=True)

    # Agregar first_order_amount
    df["first_order_amount"] = df.groupby("user_id")["amount"].transform("first")

    # Agregar last_order_amount
    df["last_order_amount"] = df.groupby("user_id")["amount"].transform("last")

    return df


def main():
    df = df_1
    df_featured = featuring(df)
    print(df_featured)


if __name__ == "__main__":
    main()
