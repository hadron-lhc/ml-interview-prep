from collections import Counter

"""
Problem 3 (Easy+)

Valid Anagram

Dadas dos strings:
    s = "listen"
    t = "silent"

Devolver True si son anagramas.
"""


def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count_s = Counter(s)
    count_t = Counter(t)

    return count_s == count_t


def main():
    s = "lssten"
    t = "silent"
    result = valid_anagram(s, t)

    print(result)


if __name__ == "__main__":
    main()
