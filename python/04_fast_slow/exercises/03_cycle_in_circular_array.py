"""
Tienes un array donde cada número indica cuántos pasos moverte:

Ejemplo:
números = [2,-1,1,2,2]

Desde índice 0:
0 → 2 → 3 → 0

Eso forma ciclo.

Return: True
"""


def solution(nums):
    n = len(nums)

    def next_index(i):
        return (i + nums[i]) % n

    for i in range(n):
        slow = i
        fast = i
        direction = nums[i]

        while True:
            slow = next_index(slow)
            fast = next_index(next_index(fast))

            if nums[slow] * direction < 0 or nums[fast] * direction < 0:
                break
            if slow == fast:
                if slow == next_index(slow):
                    break
                return True

    return False


nums = [2, -1, 1]
result = solution(nums)
print(result)
