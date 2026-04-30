"""
Problem 5 (Medium)
Longest Substring with At Most K Distinct Characters

Enunciado:
    Dado un string s y un entero k, devolver la longitud del substring más largo que contenga a lo sumo k caracteres distintos.

Ejemplos

        s = "eceba"
        k = 2

        Output: 3  -> "ece"
"""


def longest_substring_k_dist_chars(s: str, k: int) -> int:
    if k == 0:
        return 0

    if k >= len(set(s)):
        return len(s)

    freq = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


def main():
    s = "eceba"
    k = 2

    result = longest_substring_k_dist_chars(s, k)
    print(result)


if __name__ == "__main__":
    main()
