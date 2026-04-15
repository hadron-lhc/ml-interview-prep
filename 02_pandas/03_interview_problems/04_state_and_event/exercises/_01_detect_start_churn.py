"""
Objetivo

Crear:
   - is_churn_start

 True solo en la primera fila donde entra en churn

 Ejemplo
user_id | order_date | is_churn_start
------------------------------------
1       | 2023-01-01 | False
1       | 2023-01-10 | False
1       | 2023-02-15 | True   ← gap > 30 días desde la anterior
1       | 2023-03-20 | False
"""

import pandas as pd


def detect_start_of_churn(df):
    df = df.copy()

    cond = df.groupby("user_id")["timestamp"].diff() >= pd.Timedelta(days=30)
    prev = cond.groupby(df["user_id"]).shift(1).fillna(False)
    df["is_churn_start"] = cond & (~prev)

    return df
