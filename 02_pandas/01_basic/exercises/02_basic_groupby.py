from dataset import get_df


def average_salary_per_department(df):
    """
    Salario promedio agrupado
    en base al departamento
    """
    df = df.groupby("department")["salary"].mean()
    return df


def employees_per_department(df):
    """
    Contar la cantidad de
    empleados por departamento
    """
    df = df.groupby("department").size()
    return df


def agg_per_department(df):
    """
    Calcular, por departamento:
        - salario promedio
        - salario máximo
        - cantidad de empleados
    """
    df = df.groupby("department").agg(
        salario_promedio=("salary", "mean"),
        salario_maximo=("salary", "max"),
        cantidad_empleados=("salary", "size"),
    )
    return df


def main():
    df = get_df()
    df_a = average_salary_per_department(df)
    df_b = employees_per_department(df)
    df_c = agg_per_department(df)


if __name__ == "__main__":
    main()
