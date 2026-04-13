def build_features(df):
    df = df.copy()

    # 1 running total
    df["running_total"] = df.groupby("user")["amount"].cumsum()

    # 2 order count
    df["order_count"] = df.groupby("user")["order_id"].cumcount()

    # 3 previous amount

    # 4 diff

    # 5 days since last purchase

    # 6 rolling mean

    # 7 user avg

    # 8 ratio vs avg

    # 9 ranking

    # 10 category cumulative

    return df
