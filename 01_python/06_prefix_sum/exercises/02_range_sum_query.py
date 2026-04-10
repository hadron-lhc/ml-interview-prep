"""
arr = [2,4,1,6,3]

obj = NumArray(arr)

obj.sumRange(1,3)  # 4+1+6 = 11
"""


class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == "__main__":
    arr = [2, 4, 1, 6, 3]
    obj = NumArray(arr)

    print(obj.sumRange(1, 3))
