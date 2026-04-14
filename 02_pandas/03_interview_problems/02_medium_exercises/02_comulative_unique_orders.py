from dataset import df_1
import pandas as pd

"""
Objetivo

Crear:
   - order_number

(la orden 1, 2, 3… por usuario)

Output esperado
user_id | order_date | order_number
----------------------------------
1       | 2023-01-01 | 1
1       | 2023-01-10 | 2
1       | 2023-02-01 | 3
"""


def featuring(df):
    df = df.copy()
    # Ordenar fecha
    df["order_date"] = pd.to_datetime(df["order_date"])
    df = df.sort_values(["user_id", "order_date"]).reset_index(drop=True)

    # Agregar feature
    df["order_number"] = df.groupby("user_id").cumcount() + 1

    return df


def main():
    df = df_1
    df_featured = featuring(df)
    print(df_featured)


if __name__ == "__main__":
    main()
