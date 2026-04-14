from dataset import df_1

"""
Objetivo

Crear:

    - is_top_20pct_user
"""


def featuring(df):
    df = df.copy()

    total = df.groupby("user_id")["amount"].sum()

    threshold = total.quantile(0.8)

    power_users = total >= threshold

    df["is_top_20pct_user"] = df["user_id"].map(power_users)


def main():
    df = df_1
    df_featured = featuring(df)
    print(df_featured)


if __name__ == "__main__":
    main()
