"""
Find the two most frequent word
"""


def solution(words, k):
    count = {}

    for word in words:
        count[word] = count.get(word, 0) + 1

    top_k = sorted(count.items(), key=lambda item: item[1], reverse=True)[:k]
    return top_k


def main():
    words = ["a", "b", "a", "c", "b", "a"]
    result = solution(words)
    print(result)


if __name__ == "__main__":
    main()
