"""
Longest substring without repeating characters

input: abcabcbb
output: 3 (abc)
"""


def solution(s):
    char_set = set()
    left = 0
    start = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        if right - left + 1 > max_length:
            max_length = right - left + 1
            start = left

    return max_length, s[start : start + max_length]


result = solution("abcbb")
print(result)
