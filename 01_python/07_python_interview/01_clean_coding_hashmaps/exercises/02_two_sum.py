"""
Two Sum

Dado:
    nums = [2,7,11,15]
    target = 9

Devolver índices de dos números que sumen target.

Resultado: [0,1]
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    prev_map = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[num] = i

    return []


def main():
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(result)


if __name__ == "__main__":
    main()
