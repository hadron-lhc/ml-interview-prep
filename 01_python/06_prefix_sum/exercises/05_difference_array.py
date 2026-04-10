"""
Tenés un array de tamaño n:
n = 5
arr = [0,0,0,0,0]

Y queries:
updates = [
    (1,3,2),  # sumar +2 desde índice 1 a 3
    (2,4,3)   # sumar +3 desde índice 2 a 4
]

Output esperado:
[0,2,5,5,3]
"""


def solution(n, updates):
    diff = [0] * n

    for left, right, val in updates:
        diff[left] += val

        if right + 1 < n:
            diff[right + 1] -= val

    result = [0] * n
    result[0] = diff[0]

    for i in range(1, n):
        result[i] += result[i - 1] + diff[i]

    return result


def main():
    n = 5
    updates = [(1, 3, 2), (2, 4, 3)]
    result = solution(n, updates)
    print(result)


if __name__ == "__main__":
    main()
