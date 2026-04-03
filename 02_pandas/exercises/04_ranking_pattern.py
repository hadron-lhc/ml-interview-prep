import pandas as pd
from dataset import get_df

"""
Agregar columna:
salary_rank_inside_department

Ejemplo:
IT:
Pedro   8000   rank 1
Juan    5500   rank 2
Sofia   5000   rank 3
Ana     4000   rank 4

"""


def solution(df):
    df = df.copy()
    df["salary_rank_inside_department"] = df.groupby("department")["salary"].rank(
        ascending=False
    )
    df["top_earner_flag"] = df["salary_rank_inside_department"] == 1
    return df


def main():
    df = get_df()
    df_result = solution(df)
    print(df_result)


if __name__ == "__main__":
    main()
