"""Find Middle Element"""


def solution(nums):
    slow = fast = 0

    while fast < len(nums) - 1:
        slow += 1
        fast += 2

    return nums[slow]


nums = [1, 2, 3, 4]
# Output esperado: 3 (elemento del medio)
print(solution(nums))
