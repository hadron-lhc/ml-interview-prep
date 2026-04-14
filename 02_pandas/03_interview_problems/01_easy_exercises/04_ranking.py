from dataset import df_1
import pandas as pd

"""
Objetivo

Crear:
    - order_rank_by_amount

Ranking por amount dentro de cada usuario
(1 = mayor compra)

Output esperado
user_id | amount | order_rank_by_amount
---------------------------------------
1       | 200    | 1
1       | 150    | 2
1       | 100    | 3
"""


def featuring(df):
    df = df.copy()

    # Agregar order_rank_by_amount
    df["order_rank_by_amount"] = df.groupby("user_id")["amount"].rank(
        method="dense", ascending=False
    )

    return df


def main():
    df = df_1

    df_featured = featuring(df)
    print(df_featured)


if __name__ == "__main__":
    main()
