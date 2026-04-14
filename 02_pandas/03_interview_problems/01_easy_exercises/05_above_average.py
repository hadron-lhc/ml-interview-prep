from dataset import df_1

"""
Objetivo

Crear una columna:

above_user_avg (True/False)
Output esperado
user_id | amount | above_user_avg
--------------------------------
1       | 100    | False
1       | 150    | False
1       | 200    | True
"""


def featuring(df):
    df = df.copy()

    # Agregar columna average
    df["above_user_avg"] = df["amount"] > df.groupby("user_id")["amount"].transform(
        "mean"
    )

    return df


def main():
    df = df_1

    df_featured = featuring(df)
    print(df_featured)


if __name__ == "__main__":
    main()
