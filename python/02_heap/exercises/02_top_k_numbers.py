import heapq

"""
Top K numbers

   input: nums=[4,1,6,3,8,2]
          k=3

   output: [8,6,4]
"""


def top_k_numbers(nums, k):
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappushpop(heap, num)

    result = sorted(heap, reverse=True)
    return result


nums = [4, 1, 6, 3, 8, 2]
k = 3
top_k = top_k_numbers(nums, k)
print(top_k)
