from dataset import df_1
import pandas as pd

"""
Objetivo

Crear:
   - rolling_sum_3_orders

Output esperado
user_id | amount | rolling_sum_3_orders
--------------------------------------
1       | 100    | 100
1       | 150    | 250
1       | 200    | 450
"""


def featuring(df):
    # Ordenar fecha
    df["order_date"] = pd.to_datetime(df["order_date"])
    df = df.sort_values(["user_id", "order_date"]).reset_index(drop=True)

    # Agregar feature
    df["rolling_sum_3_orders"] = (
        df.groupby("user_id")["amount"]
        .rolling(window=3, min_periods=1)
        .sum()
        .reset_index(level=0, drop=True)
    )

    return df


def main():
    df = df_1
    df_featured = featuring(df)
    print(df_featured)


if __name__ == "__main__":
    main()
