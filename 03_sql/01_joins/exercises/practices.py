import sqlite3


def run_schema(cursor):
    with open("schema.sql", "r") as f:
        cursor.executescript(f.read())


def run_exercises(cursor):
    with open("exercises.sql", "r") as f:
        queries = f.read().split(";")

        for i, query in enumerate(queries):
            query = query.strip()

            if query == "":
                continue

            print("\n====================")
            print(f"EXERCISE BLOCK {i + 1}")
            print("====================")

            try:
                result = cursor.execute(query)

                rows = result.fetchall()

                for row in rows:
                    print(row)

            except Exception as e:
                print("ERROR:")
                print(e)


def main():
    conn = sqlite3.connect(":memory:")

    cursor = conn.cursor()

    run_schema(cursor)

    run_exercises(cursor)

    conn.close()


if __name__ == "__main__":
    main()
