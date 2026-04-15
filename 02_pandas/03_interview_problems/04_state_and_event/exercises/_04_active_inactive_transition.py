"""
Contexto

Un usuario está:
    activo si compra en los últimos 30 días
    inactivo si no

Objetivo
    - became_inactive

True cuando pasa de activo → inactivo
"""


def became_inactive(df):
    df = df.copy()
    days = df.groupby("user_id")["timestamp"].diff().dt.days

    active = days <= 30

    prev_active = active.groupby(df["user_id"]).shift(1)

    df["became_inactive"] = (prev_active == True) & (active == False)

    return df
