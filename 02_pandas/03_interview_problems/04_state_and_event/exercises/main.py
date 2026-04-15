import pandas as pd
from _01_detect_start_churn import detect_start_of_churn
from _02_sessionizarion import add_sessions
from _03_first_purchase_after_sigup import first_purchase
from _04_active_inactive_transition import became_inactive
from _05_consecutive_event_block import get_block_id
from dataset import df_1, users


def main():
    df = df_1
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    users["signup_date"] = pd.to_datetime(users["signup_date"])

    df = df.sort_values(["user_id", "timestamp"]).reset_index(drop=True)

    """
    # Primer ejercicio
    df_featured_1 = detect_start_of_churn(df)
    print(df_featured_1)
    """

    """
    # Segundo ejercicio
    df_featured_2 = add_sessions(df)
    print(df_featured_2)
    """

    """
    # Tercer ejercicio
    df_featured_3 = first_purchase(df, users)
    print(df_featured_3)
    """

    """
    # Cuarto ejercicio
    df_featured_4 = became_inactive(df)
    print(df_featured_4)
    """

    # Quinto ejercicio
    df_featured_5 = get_block_id(df)
    print(df_featured_5)


if __name__ == "__main__":
    main()
