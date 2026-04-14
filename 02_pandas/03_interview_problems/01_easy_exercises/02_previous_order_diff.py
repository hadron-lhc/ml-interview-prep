import pandas as pd
from dataset import df_1

"""
Objetivo

Crear una columna:

    diff_from_prev_order


Que sea:

    current_amount - previous_amount

Output esperado:
user_id | order_date | amount | diff_from_prev_order
---------------------------------------------------
1       | 2023-01-01 | 100    | NaN
1       | 2023-01-10 | 150    | 50
1       | 2023-02-01 | 200    | 50
"""


def featuring(df):
    df = df.copy()

    # Ordenar por fecha
    df["date"] = pd.to_datetime(df["order_date"])
    df = df.sort_values(["user_id", "order_date"]).reset_index(drop=True)

    # Agregar columna de diff
    df["prev_value"] = df.groupby("user_id")["amount"].shift(1)
    df["diff_from_prev_order"] = df["amount"] - df["prev_value"]
    df.drop(columns=["prev_value"], inplace=True)

    return df


def main():
    df = df_1
    df_featured = featuring(df)
    print(df_featured)


if __name__ == "__main__":
    main()
