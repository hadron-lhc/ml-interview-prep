"""
Problem 6 (Medium / Data Useful)
Join Two Lists by id

Tenés:
    users = [
        {"id": 1, "name": "Ana"},
        {"id": 2, "name": "Juan"}
    ]

    orders = [
        {"id": 1, "amount": 100},
        {"id": 1, "amount": 50},
        {"id": 2, "amount": 80}
    ]

Output:

    [
        {"id":1, "name":"Ana", "orders":[100,50]},
        {"id":2, "name":"Juan", "orders":[80]}
    ]

"""

from collections import defaultdict


def join_two_tables(users, orders):
    orders_per_user = defaultdict(list)
    for order in orders:
        orders_per_user[order["id"]].append(order["amount"])

    result = []

    for user in users:
        user_id = user["id"]
        new_item = {
            "id": user_id,
            "name": user["name"],
            "orders": orders_per_user[user_id],
        }
        result.append(new_item)

    return result


def main():
    users = [{"id": 1, "name": "Ana"}, {"id": 2, "name": "Juan"}]

    orders = [
        {"id": 1, "amount": 100},
        {"id": 1, "amount": 50},
        {"id": 2, "amount": 80},
    ]

    df = join_two_tables(users, orders)
    print(df)


if __name__ == "__main__":
    main()
