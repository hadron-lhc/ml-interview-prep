from dataset import df_1

"""
Objetivo

Crear:
   - pct_of_user_total

Output esperado
user_id | amount | pct_of_user_total
-----------------------------------
1       | 100    | 0.22
1       | 150    | 0.33
1       | 200    | 0.44
"""


def featuring(df):
    df["pct_of_user_total"] = df["amount"] / df.groupby("user_id")["amount"].transform(
        "sum"
    )
    return df


def main():
    df = df_1
    df_featured = featuring(df)
    print(df_featured)


if __name__ == "__main__":
    main()
