"""
Contexto

Un usuario entra en churn si pasan ≥ 30 días sin actividad.
PERO ahora hay una condición más realista:

* Solo queremos marcar churn si después vuelve

Objetivo
    - is_real_churn_start

 -> True solo si:

    hubo gap ≥ 30 días
    Y ese gap está entre dos eventos (no al final del dataset)

Ejemplo
user_id | dates
-------------------------
1       | Jan 1
1       | Jan 10
1       | Feb 20  ← gap > 30 → churn start ✅
1       | Mar 1

2       | Jan 1
2       | Mar 10  ← gap > 30 pero no vuelve → ❌ NO marcar
"""

from dataset import df_1
import pandas as pd


def featured(df):
    diff = df.groupby("user_id")["timestamp"].diff()

    cond = diff >= pd.Timedelta(days=30)

    prev = cond.groupby(df["user_id"]).shift(1).fillna(False)

    has_post = df.groupby("user_id")["timestamp"].shift(-1).notna()

    df["is_real_churn_start"] = cond & (~prev) & has_post

    return df


def main():
    df = df_1.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values(["user_id", "timestamp"]).reset_index(drop=True)

    df_featured = featured(df)
    print(df_featured)


if __name__ == "__main__":
    main()
