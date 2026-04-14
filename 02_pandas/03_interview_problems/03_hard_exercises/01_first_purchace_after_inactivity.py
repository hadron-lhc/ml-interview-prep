from itertools import groupby
from dataset import df_1
import pandas as pd

"""
Contexto

   - Queremos detectar cuando un usuario vuelve después de estar inactivo.

Definición

   - Un usuario está “inactivo” si pasan ≥ 30 días sin comprar.

Objetivo

    Crear:
       - is_return_after_30d

Output esperado (conceptual)
user_id | order_date | is_return_after_30d
-----------------------------------------
1       | ...        | False
1       | ...        | False
1       | ...        | True   ← volvió después de 30 días
"""


def featuring(df):
    df = df.copy()

    df["order_date"] = pd.to_datetime(df["order_date"])
    df = df.sort_values(["user_id", "order_date"]).reset_index(drop=True)

    df["is_return_after_30d"] = df.groupby("user_id")[
        "order_date"
    ].diff() > pd.Timedelta(days=30)

    return df


def main():
    df = df_1
    df_featured = featuring(df)
    print(df_featured)


if __name__ == "__main__":
    main()
