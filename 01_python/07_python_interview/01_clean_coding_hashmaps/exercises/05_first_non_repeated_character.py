""" "
Problem 5 (Medium Easy)
First Non-Repeated Character

Dado:
    s = "leetcode"

Devolver primer carácter que no se repite: "l"

Si no existe: ""
"""

from collections import Counter


def first_non_repeated_character(s):
    counts = Counter(s)

    for char in s:
        if counts[char] == 1:
            return char

    return ""


def main():
    s = "leetcode"
    result = first_non_repeated_character(s)
    print(result)


if __name__ == "__main__":
    main()
