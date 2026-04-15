import pandas as pd

df_1 = pd.DataFrame(
    {
        "user_id": [1, 1, 1, 1, 2, 2, 2, 3, 3, 3],
        "timestamp": [
            "2023-01-01",
            "2023-01-10",
            "2023-02-20",  # gap > 30 → inactive antes
            "2023-02-25",  # reactivated
            "2023-01-01",
            "2023-03-10",  # vuelve después de mucho
            "2023-03-15",
            "2023-01-01",
            "2023-01-20",
            "2023-01-25",
        ],
    }
)
