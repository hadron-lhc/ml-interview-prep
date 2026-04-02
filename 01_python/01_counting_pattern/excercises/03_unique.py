"""
Find unique elements
"""


def solution(nums):
    count = {}
    unique_elements = []
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for key, value in count.items():
        if value == 1:
            unique_elements.append(key)
    return unique_elements


def main():
    nums = [1, 2, 2, 3, 4, 4]
    result = solution(nums)
    print(result)


if __name__ == "__main__":
    main()
