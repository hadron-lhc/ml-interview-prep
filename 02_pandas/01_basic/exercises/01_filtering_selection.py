from dataset import get_df


def filtering_age(df):
    """
    Filtrar empleados con edad mayor a 30
    """
    df = df.copy()
    df = df[df["age"] > 30]
    return df


def filtering_department(df):
    """
    Filtrar departamento igual a IT
    Y mostrar solo name y salary
    """
    df = df.copy()
    df = df[df["department"] == "IT"]
    df = df[["name", "salary"]]
    return df


def multiple_filter(df):
    """
    Filtrar: salary > 5000 AND age < 40
    """
    df = df.copy()
    df = df[(df["age"] < 40) & (df["salary"] > 5000)]
    return df


def main():
    df = get_df()
    df_a = filtering_age(df)
    df_b = filtering_department(df)
    df_c = multiple_filter(df)


if __name__ == "__main__":
    main()
