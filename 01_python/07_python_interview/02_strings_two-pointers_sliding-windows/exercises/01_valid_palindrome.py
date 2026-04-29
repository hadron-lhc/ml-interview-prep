"""
Problem 1 (Easy)

Valid Palindrome

Dado un string s, devolver True si es palíndromo y False si no.

Reglas:
    - ignorar espacios
    - ignorar símbolos
    - ignorar mayúsculas/minúsculas
"""


def is_palindrome(s: str) -> bool:
    s = s.lower()
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


def main():
    s = " "

    result = is_palindrome(s)
    print(result)


if __name__ == "__main__":
    main()
