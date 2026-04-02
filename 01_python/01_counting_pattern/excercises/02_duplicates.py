"""
Find Duplicates in nums
"""


def solution(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


def main():
    nums = [1, 2, 3, 1, 2, 4]
    result = solution(nums)
    print(result)


if __name__ == "__main__":
    main()
