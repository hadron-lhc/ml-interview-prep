"""
Objetivo

Crear:

session_id

Ej:

user_id | timestamp           | session_id
------------------------------------------
1       | 10:00               | 1
1       | 10:10               | 1
1       | 11:00               | 2  ← nueva sesión
"""

import pandas as pd


def add_sessions(df):
    df = df.copy()

    df["session_id"] = (
        df.groupby("user_id")["timestamp"]
        .diff()
        .ge(pd.Timedelta(minutes=30))
        .groupby(df["user_id"])
        .cumsum()
        + 1
    )

    return df
