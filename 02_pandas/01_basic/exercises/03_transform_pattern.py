"""
Agregar la columna:
 diff (salary vs department_avg)

 Bonus:
 is_above_department_avg (True/False)
"""

from dataset import get_df


def add_cols(df):
    df = df.copy()
    dept_avg = df.groupby("department")["salary"].transform("mean")

    df["department_avg"] = dept_avg
    df["diff"] = df["salary"] - dept_avg
    df["is_above_department_avg"] = df["salary"] > dept_avg

    return df[
        [
            "name",
            "salary",
            "department",
            "department_avg",
            "diff",
            "is_above_department_avg",
        ]
    ]


def main():
    df = get_df()
    df_result = add_cols(df)
    print(df_result)


if __name__ == "__main__":
    main()
