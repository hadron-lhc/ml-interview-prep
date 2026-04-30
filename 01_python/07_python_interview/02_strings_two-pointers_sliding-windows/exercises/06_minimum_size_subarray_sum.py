"""
Problem 6
Minimum Size Subarray Sum

Enunciado:

    Dado un array de enteros positivos nums y un entero target, devolver:
    la longitud mínima de un subarray continuo cuya suma sea ≥ target

    Si no existe: 0

Ejemplos

    nums = [2,3,1,2,4,3]
    target = 7

    Output: 2
    Porque [4,3] suma 7
"""


def minimum_size_subarray(nums: list[int], target: int) -> int:
    min_len = float("inf")

    left = 0
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)

            if min_len == 1:
                return 1

            current_sum -= nums[left]
            left += 1

    if min_len == float("inf"):
        return 0

    return min_len


def main():
    nums = [2, 3, 1, 2, 4, 3]
    target = 7

    result = minimum_size_subarray(nums, target)
    print(result)


if __name__ == "__main__":
    main()
