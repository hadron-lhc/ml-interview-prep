from pandas.core import window
from dataset import df_1
import pandas as pd

"""
Objetivo

Crear:
    - rolling_avg_2_orders

Promedio de las últimas 2 órdenes del usuario (incluyendo la actual)

Output esperado
user_id | order_date | amount | rolling_avg_2_orders
----------------------------------------------------
1       | 2023-01-01 | 100    | 100
1       | 2023-01-10 | 150    | 125
1       | 2023-02-01 | 200    | 175
"""


def featuring(df):
    df = df.copy()

    # Ordenar por fecha
    df["order_date"] = pd.to_datetime(df["order_date"])
    df = df.sort_values(["user_id", "order_date"]).reset_index(drop=True)

    # Agregar rolling_avg_2_orders
    df["rolling_avg_2_orders"] = (
        df.groupby("user_id")["amount"]
        .rolling(window=2, min_periods=1)
        .mean()
        .reset_index(level=0, drop=True)
    )

    return df


def main():
    df = df_1

    df_featured = featuring(df)
    print(df_featured)


if __name__ == "__main__":
    main()
