from dataset import df_1
import pandas as pd


def featuring(df):
    # is_active -> actividad en los ultimos 30 dias
    # is_reactive -> cuando pasa de inactivo a activo
    days = df.groupby("user_id")["timestamp"].diff().dt.days

    is_active = days.le(30) | days.isna()

    prev_active = is_active.groupby(df["user_id"]).shift(1).fillna(True)

    is_reactive = (~prev_active) & is_active

    df["is_active"] = is_active
    df["is_reactive"] = is_reactive

    return df


def main():
    df = df_1.copy()

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values(["user_id", "timestamp"]).reset_index(drop=True)

    df_featured = featuring(df)
    print(df_featured)


if __name__ == "__main__":
    main()
