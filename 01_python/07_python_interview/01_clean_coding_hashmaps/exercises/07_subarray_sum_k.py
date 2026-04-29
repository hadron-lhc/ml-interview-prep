"""
Problem 7 (Hard Intro)

Subarray Sum = K

Dado:
        nums = [1,1,1]
        k = 2

Cantidad de subarrays continuos cuya suma sea 2


Resultado: 2

Porque:
        [1,1] (pos 0-1)
        [1,1] (pos 1-2)
"""


def solution(nums, k):
    count = {0: 1}
    prefix_sum = 0
    result = 0

    for num in nums:
        prefix_sum += num
        result += count.get(prefix_sum - k, 0)
        count[prefix_sum] = count.get(prefix_sum, 0) + 1

    return result


def main():
    nums = [1, 1, 1]
    k = 2

    result = solution(nums, k)
    print(result)


if __name__ == "__main__":
    main()
