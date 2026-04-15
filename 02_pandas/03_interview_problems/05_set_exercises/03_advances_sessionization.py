from dataset import df_1
import pandas as pd

"""
Contexto

Queremos construir sesiones, pero ahora con una regla más compleja:

Reglas

Una nueva sesión empieza si:

    1. pasan ≥ 30 minutos
    ó
    2. cambia el día (aunque no pasen 30 minutos)

Objetivo
    - session_id

Ejemplo:

timestamp
-------------------
2023-01-01 23:50
2023-01-02 00:05  ← nuevo día → nueva sesión
"""


def add_sessions(df):
    diff = df.groupby("user_id")["timestamp"].diff()

    time_gap = diff >= pd.Timedelta(minutes=30)

    day_change = (
        df["timestamp"].dt.date != df.groupby("user_id")["timestamp"].shift(1).dt.date
    )

    new_session = time_gap | day_change

    new_session = new_session.fillna(True)

    df["session_id"] = new_session.groupby(df["user_id"]).cumsum()

    return df


def main():
    df = df_1.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values(["user_id", "timestamp"]).reset_index(drop=True)

    df_featured = add_sessions(df)
    print(df_featured)


if __name__ == "__main__":
    main()
