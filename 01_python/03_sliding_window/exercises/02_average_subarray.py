"""
Average subarray size K

nums = [2, 1, 5, 1, 3, 2]
k = 3

Output: [2.6, 2.3, 3, 2]

"""


def solution(nums, k):
    if k > len(nums):
        return []

    window_sum = sum(nums[:k])
    averages = [round(window_sum / k, 2)]
    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i - k]

        averages.append(round(window_sum / k, 2))

    return averages


nums = [2, 1, 5, 1, 3, 2]
k = 3

result = solution(nums, k)
print(result)
