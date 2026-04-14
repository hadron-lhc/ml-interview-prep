from dataset import df_1

"""
Objetivo

Crear:
   - is_first_time_above_150

Solo debe ser True en la primera vez que el usuario supera 150.

Output esperado
user_id | amount | is_first_time_above_150
-----------------------------------------
1       | 100    | False
1       | 150    | False
1       | 200    | True
1       | 180    | False
"""


def featuring(df):
    cond = df["amount"] > 150

    df["is_first_time_above_150"] = cond & (
        df.groupby("user_id")["amount"].cummax().shift(1).fillna(0) <= 150
    )

    return df


def main():
    df = df_1
    df_featured = featuring(df)
    print(df_featured)


if __name__ == "__main__":
    main()
