import sqlite3


def run():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    # Load schema
    with open("schema.sql", "r") as f:
        cur.executescript(f.read())

    # Run exercises
    with open("exercises.sql", "r") as f:
        queries = f.read().split(";")

    for i, q in enumerate(queries):
        q = q.strip()
        if not q:
            continue

        print(f"\n--- Query {i + 1} ---")
        try:
            cur.execute(q)
            rows = cur.fetchall()
            for r in rows[:10]:
                print(r)
        except Exception as e:
            print("Error:", e)

    conn.close()


if __name__ == "__main__":
    run()
