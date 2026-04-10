"""
Dado:
nums = [1,2,3]
k = 3

Encontrar:
cuántos subarrays suman exactamente k.

Output: 2
"""


def solution_optimized(nums, k):
    count = {0: 1}
    result = 0
    prefix_sum = 0

    for num in nums:
        prefix_sum += num
        result += count.get(prefix_sum - k, 0)
        count[prefix_sum] = count.get(prefix_sum, 0) + 1

    return result


def main():
    nums = [1, 2, 3]
    k = 3

    result = solution_optimized(nums, k)
    print(result)


if __name__ == "__main__":
    main()
