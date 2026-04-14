"""
Contexto

Tenés:
    tabla de usuarios (signup_date)
    tabla de órdenes

Queremos detectar la primera compra después del signup

Objetivo
    - is_first_purchase_after_signup
"""

import pandas as pd


def first_purchase(df, users):
    df_merged = pd.merge(df, users, on="user_id", how="inner")

    after_signup = df_merged[df_merged["timestamp"] > df_merged["signup_date"]]
    first_idx = after_signup.groupby("user_id")["timestamp"].idxmin()

    df_merged["is_first_purchase_after_signup"] = False
    df_merged.loc[first_idx, "is_first_purchase_after_signup"] = True

    return df_merged
