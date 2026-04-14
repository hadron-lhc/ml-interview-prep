from dataset import df_1
import pandas as pd

"""
Contexto

Feature muy usada en modelos de churn.

Objetivo
   - days_until_next_order
"""


def featuring(df):
    df = df.copy()

    df["order_date"] = pd.to_datetime(df["order_date"])
    df = df.sort_values(["user_id", "order_date"]).reset_index(drop=True)

    df["days_until_next_order"] = (
        df.groupby("user_id")["order_date"].shift(-1) - df["order_date"]
    ).dt.days

    return df


def main():
    df = df_1
    df_featured = featuring(df)
    print(df_featured)


if __name__ == "__main__":
    main()
