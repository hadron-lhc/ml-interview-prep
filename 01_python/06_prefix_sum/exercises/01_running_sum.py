"""
[1,2,3,4] → [1,3,6,10]
"""


def running_sum(arr):
    prefix = []
    current = 0

    for num in arr:
        current += num
        prefix.append(current)

    return prefix


def main():
    arr = [1, 2, 3, 4]
    prefix = running_sum(arr)
    print(prefix)


if __name__ == "__main__":
    main()
