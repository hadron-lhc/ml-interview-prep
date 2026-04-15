import pandas as pd

df_1 = pd.DataFrame(
    {
        "user_id": [
            # USER 1
            1,
            1,
            1,
            1,
            1,
            1,
            # USER 2 (no vuelve después de churn)
            2,
            2,
            # USER 3 (muchos cambios de día)
            3,
            3,
            3,
            3,
            3,
            # USER 4 (ideal para streaks)
            4,
            4,
            4,
            4,
            4,
            4,
        ],
        "timestamp": [
            # USER 1
            "2023-01-01 10:00",
            "2023-01-01 10:20",
            "2023-01-01 11:00",
            "2023-02-15 09:00",  # gap > 30 → churn candidate
            "2023-02-16 10:00",
            "2023-03-20 12:00",
            # USER 2 (NO vuelve después del gap)
            "2023-01-05 14:00",
            "2023-03-10 16:00",  # gap > 30 pero no hay siguiente
            # USER 3 (cambio de día frecuente)
            "2023-01-01 23:50",
            "2023-01-02 00:10",  # nuevo día
            "2023-01-02 00:20",
            "2023-01-03 00:05",  # nuevo día
            "2023-01-03 00:25",
            # USER 4 (streaks)
            "2023-01-01 08:00",
            "2023-01-01 09:00",
            "2023-01-01 10:00",
            "2023-01-01 11:00",
            "2023-01-01 12:00",
            "2023-01-01 13:00",
        ],
        "amount": [
            # USER 1
            50,
            70,
            120,
            80,
            90,
            200,
            # USER 2
            40,
            300,
            # USER 3
            20,
            25,
            30,
            35,
            40,
            # USER 4 (para streak)
            100,
            120,
            140,
            130,
            150,
            170,
        ],
    }
)
