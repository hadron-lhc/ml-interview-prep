"""
Max sum subarray size K

nums = [2, 1, 5, 1, 3, 2]
k = 3

Output: 9

"""


def solution(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i - k]
        max_sum = max(window_sum, max_sum)

    return max_sum


nums = [2, 1, 5, 1, 3, 2]
k = 3

result = solution(nums, k)
print(result)
