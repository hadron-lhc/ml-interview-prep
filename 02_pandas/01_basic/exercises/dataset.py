import pandas as pd


def get_df():
    df = pd.DataFrame(
        {
            "name": ["Ana", "Luis", "Sofia", "Pedro", "Juan"],
            "age": [23, 35, 29, 42, 31],
            "salary": [4000, 6000, 5000, 8000, 5500],
            "department": ["IT", "HR", "IT", "Management", "IT"],
        }
    )
    return df
