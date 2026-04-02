"""
Dado un string s y un entero k, podes
reemplazar como máximo k caracteres
por cualquier otro.

Encontrar la longitud del sub-string mas largo
que pueda transformarse en un string con todos
sus caracteres iguales.
"""


def solution(s, k):
    freq = {}
    left = 0
    max_freq = 0
    max_length = 0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        max_freq = max(max_freq, freq[s[right]])
        while (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length


# input:
s: str = "AABBAB"
k: int = 1

# output esperado:
# 4

print(solution(s, k))
