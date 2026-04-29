"""
Two Sum II (Sorted Array)

Dado un array ordenado ascendentemente:

    numbers = [2,7,11,15]
    target = 9

Devolver los índices (1-indexed) de dos números que suman target.

Resultado: [1,2]

Porque:
    2 + 7 = 9
"""


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    left = 0
    right = len(nums) - 1

    while left < right:
        curr_sum = nums[left] + nums[right]

        if curr_sum > target:
            right -= 1
        elif curr_sum < target:
            left += 1
        else:
            return (left + 1, right + 1)

    return ()


def main():
    nums = [3, 7, 11, 15]
    target = 22

    result = two_sum(nums, target)
    print(result)


if __name__ == "__main__":
    main()
