from collections import Counter


def counting_frequency_dict(words):
    frequency = {}
    for ch in words:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    return frequency


def counting_frequency_get(words):
    frequency = {}
    for ch in words:
        frequency[ch] = frequency.get(ch, 0) + 1
    return frequency


def counting_frequency_count(words):
    frequency = Counter(words)
    return frequency


def main():
    words = ["a", "b", "a", "c", "b", "a"]
    first_result = counting_frequency_dict(words)
    second_result = counting_frequency_get(words)
    third_result = counting_frequency_count(words)


if __name__ == "__main__":
    main()
