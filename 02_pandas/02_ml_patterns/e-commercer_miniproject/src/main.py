from pathlib import Path
from dataset import df
from featuring import build_features

DATA_PATH = Path(__file__).parent.parent / "data"


def main():
    df_raw = df
    print(df_raw)

    # Guardar en data
    try:
        df_raw.to_csv(DATA_PATH / "data_raw.csv", index=False, encoding="UTF-8")
        print(f"Data raw guardada correctamente en {DATA_PATH}/data_raw.csv")

        # Aregegar featuring
        df_featured = build_features(df_raw)
        df_featured.to_csv(
            DATA_PATH / "data_featured.csv", index=False, encoding="UTF-8"
        )
        print(
            f"Data post featuring guardada correctamente en {DATA_PATH}/data_featured.csv"
        )

    except Exception as e:
        print(f"error: {e}")
        return


if __name__ == "__main__":
    main()
