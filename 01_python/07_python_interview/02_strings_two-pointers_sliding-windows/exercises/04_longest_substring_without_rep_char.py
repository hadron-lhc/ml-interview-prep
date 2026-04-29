"""
Problem 4
Longest Substring Without Repeating Characters

Enunciado:

    Dado un string s, devolver la longitud del substring más largo sin caracteres repetidos.

Ejemplos:
        s = "abcabcbb"
        Output: 3  -> "abc"
"""


def longest_substring_length(s: str) -> int:
    seen = set()
    left = 0
    max_long = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_long = max(max_long, right - left + 1)

    return max_long


def main():
    s = "abcabcbb"
    result = longest_substring_length(s)
    print(result)


if __name__ == "__main__":
    main()
