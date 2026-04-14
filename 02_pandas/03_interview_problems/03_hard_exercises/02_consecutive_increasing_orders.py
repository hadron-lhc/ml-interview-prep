from dataset import df_1
import pandas as pd

"""
Contexto

Queremos detectar rachas donde el usuario va aumentando gasto consecutivamente.

Objetivo

Crear:
    - is_increasing_streak

True si:
amount > previous_amount

Bonus (difícil)

Crear:
    - streak_length

Ej:

100 → 120 → 150 → 130
 F      T      T      F
 0      1      2      0
"""


def featuring(df):
    df = df.copy()

    df["order_date"] = pd.to_datetime(df["order_date"])
    df = df.sort_values(["user_id", "order_date"]).reset_index(drop=True)

    inc = df.groupby("user_id")["amount"].diff() > 0

    streak_id = (~inc).cumsum()

    df["streak_length"] = inc.groupby([df["user_id"], streak_id]).cumsum()

    return df


def main():
    df = df_1
    df_featured = featuring(df)
    print(df_featured)


if __name__ == "__main__":
    main()
