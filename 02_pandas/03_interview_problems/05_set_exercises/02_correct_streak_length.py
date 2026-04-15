"""
Contexto

Queremos calcular correctamente la longitud de rachas donde:

amount > previous_amount

Objetivo
    - streak_length

Ejemplo
amount: 100, 120, 150, 130, 140, 160

inc:    F,   T,   T,   F,   T,   T
streak: 0,   1,   2,   0,   1,   2
"""

from dataset import df_1


def streak_length(df):
    inc = df.groupby("user_id")["amount"].diff() > 0

    group = (~inc).groupby(df["user_id"]).cumsum()

    df["streak_length"] = inc.groupby([df["user_id"], group]).cumsum()

    return df


def main():
    df = df_1.copy()
    df_featured = streak_length(df)
    print(df_featured)


if __name__ == "__main__":
    main()
