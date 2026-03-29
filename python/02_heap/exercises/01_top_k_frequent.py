import heapq


def top_k_frequent(words, k):
    if k <= 0:
        return []

    if not words:
        return []

    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1

    heap = []

    for word, freq in count.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, word))
        else:
            if freq > heap[0][0]:
                heapq.heappushpop(heap, (freq, word))

    return [word for freq, word in heap]


words = ["ml", "nlp", "rag", "rag", "ml", "ml", "hola", "ey"]
heap = top_k_frequent(words, 3)

print(heap)
