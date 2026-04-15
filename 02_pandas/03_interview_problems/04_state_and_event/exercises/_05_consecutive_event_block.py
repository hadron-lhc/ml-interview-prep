"""
Contexto

Queremos agrupar bloques consecutivos donde:

amount > 100

Objetivo
Crear:
    - block_id

Ej:
amount: 50, 120, 130, 80, 140, 150
block:   0,   1,   1,  0,   2,   2
"""


def get_block_id(df):
    df = df.copy()

    cond = df["amount"] > 100

    group = (~cond).groupby(df["user_id"]).cumsum()

    df["block_id"] = cond.groupby([df["user_id"], group]).cumsum()

    return df
