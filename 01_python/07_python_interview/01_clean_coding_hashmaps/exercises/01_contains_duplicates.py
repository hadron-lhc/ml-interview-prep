"""
Problem 1 (Easy)
Contains Duplicate

Dado un array de enteros nums, devolvé:

    - True: si algún valor aparece al menos dos veces
    - False: si todos son únicos
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def main():
    nums = [1, 2, 3, 1]
    result = contains_duplicate(nums)
    print(result)


if __name__ == "__main__":
    main()
