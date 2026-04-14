import pandas as pd


def build_features(df):
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])

    df = df.sort_values(["user", "date"]).reset_index(drop=True)

    # 1 running total
    df["running_total"] = df.groupby("user")["amount"].cumsum()

    # 2 order count
    df["order_count"] = df.groupby("user").cumcount() + 1

    # 3 previous amount
    df["prev_amount"] = df.groupby("user")["amount"].shift(1)

    # 4 diff
    df["diff"] = df["amount"] - df["prev_amount"]

    # 5 days since last purchase
    df["prev_date"] = df.groupby("user")["date"].shift(1)
    df["days_since_last"] = (df["date"] - df["prev_date"]).dt.days

    df.drop(columns=["prev_date"], inplace=True)  # columna auxiliar, opcional dropearla

    # 6 rolling mean
    df["rolling_mean"] = (
        df.groupby("user")["amount"].rolling(3).mean().reset_index(level=0, drop=True)
    )

    # 7 user avg
    df["user_avg"] = df.groupby("user")["amount"].transform("mean")

    # 8 ratio vs avg
    df["ratio_vs_avg"] = df["amount"] / df["user_avg"].replace(0, 1)

    # 9 ranking
    df["ranking"] = df.groupby("user")["amount"].rank(ascending=False, method="dense")

    # 10 category cumulative
    df["category_cumulative"] = df.groupby(["user", "category"])["amount"].cumsum()

    return df
