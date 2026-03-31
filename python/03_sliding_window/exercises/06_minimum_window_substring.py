"""
Dados dos strings:

s → string principal
t → string objetivo

Encontrar el sub-string más pequeño de s que contenga todos los caracteres de t (incluyendo frecuencias).

Si no existe → devolver "".
"""


def solution(s, t):
    need_freq = {}
    window_freq = {}
    left = 0
    formed = 0

    for ch in t:
        need_freq[ch] = need_freq.get(ch, 0) + 1

    required = len(need_freq)
    min_len = float("inf")
    start = 0

    for right in range(len(s)):
        c = s[right]
        window_freq[c] = window_freq.get(c, 0) + 1
        if c in need_freq and window_freq[c] == need_freq[c]:
            formed += 1
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left

            c = s[left]
            window_freq[c] -= 1
            if c in need_freq and window_freq[s[left]] < need_freq[s[left]]:
                formed -= 1

            left += 1

    if min_len == float("inf"):
        return ""

    return s[start : start + min_len]


s: str = "ADOBECODEBANC"
t: str = "ABC"

# Output esperado: BANC

print(solution(s, t))
