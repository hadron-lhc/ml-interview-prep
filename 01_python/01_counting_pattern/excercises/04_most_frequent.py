"""
Find the most frequent word
"""


def solution(words):
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    most_frequent_word = max(count, key=count.get)
    return most_frequent_word


def main():
    words = ["ml", "nlp", "ml", "ai"]
    result = solution(words)
    print(result)


if __name__ == "__main__":
    main()
