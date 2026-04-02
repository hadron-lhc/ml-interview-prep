import heapq

"""
Top k longest words

    input:
           ["ml", "deep", "learning", "ai", "model"]
           k = 2

    output:
            ["learning", "model"]

"""


def top_k_longest_words(words, k):
    heap = []

    for word in words:
        item = (len(word), word)
        if len(heap) < k:
            heapq.heappush(heap, item)
        else:
            heapq.heappushpop(heap, item)

    return [word for _, word in heap]


words = ["ml", "deep", "learning", "ai", "model"]
k = 2

result = top_k_longest_words(words, k)
print(result)
