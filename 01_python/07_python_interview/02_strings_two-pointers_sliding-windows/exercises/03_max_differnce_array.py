"""
Problem 3 (Very Common)
Best Time to Buy and Sell Stock

Dado:
    prices = [7,1,5,3,6,4]

Max profit posible comprando una vez y vendiendo una vez después.

Resultado: 5

Porque comprar en 1 y vender en 6.
"""


def max_profit(prices):
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


def main():
    prices = [7, 1, 5, 3, 3, 4]
    result = max_profit(prices)

    print(result)


if __name__ == "__main__":
    main()
