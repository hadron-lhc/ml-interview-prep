from dataset import df_1

"""
Contexto (ML clásico)

Queremos el valor acumulado de un usuario hasta cada punto.

Objetivo
   - cumulative_revenue

Twist

Después crear:
   - pct_of_total_so_far
"""


def featuring(df):
    df = df.copy()

    df["comulative_revenue"] = df.groupby("user_id")["amount"].cumsum()

    total_user = df.groupby("user_id")["amount"].transform("sum")

    df["pct_of_total_so_far"] = df["cumulative_revenue"] / total_user

    return df


def main():
    df = df_1
    df_featured = featuring(df)
    print(df_featured)


if __name__ == "__main__":
    main()
