"""
Problem 4 (Easy / Data Style)
Group Rows by Key

Tenés:
    rows = [
        ("sales", "Ana"),
        ("tech", "Juan"),
        ("sales", "Luis"),
        ("tech", "Maria"),
    ]

Output:
    {
    "sales": ["Ana", "Luis"],
    "tech": ["Juan", "Maria"]
    }
"""

from collections import defaultdict


def group_rows(rows: list[tuple[str, str]]) -> dict[str, list[str]]:
    groups = defaultdict(list)

    for key, value in rows:
        groups[key].append(value)

    return dict(groups)


def main():
    rows = [
        ("sales", "Ana"),
        ("tech", "Juan"),
        ("sales", "Luis"),
        ("tech", "Maria"),
    ]

    result = group_rows(rows)
    print(result)


if __name__ == "__main__":
    main()
