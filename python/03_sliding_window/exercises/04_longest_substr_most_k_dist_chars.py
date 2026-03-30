"""
Dado un string s y un entero k,

Encontrar la longitud del sub-string más largo
que contenga como máximo de k caracteres distintos.
"""


def solution(s, k):
    freq = {}
    left = 0
    max_substring = ""

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        if len(s[left : right + 1]) > len(max_substring):
            max_substring = s[left : right + 1]
    return max_substring, len(max_substring)


s = "abcadcacacaca"
k = 2

result = solution(s, k)
print(result)
