"""
Un numero es happy si;
 1. Tomas sus dígitos
 2. Los elevas al cuadrado
 3. Sumas los resultados
 4. Repites el proceso con el resultado

 Si el resultado final es 1, entonces el numero es happy,
 de lo contrario no lo es
"""


def f(n):
    total = 0

    while n:
        digit = n % 10
        total += digit * digit
        n //= 10

    return total


def solution(n):
    slow = n
    fast = n

    while True:
        slow = f(slow)
        fast = f(f(fast))

        if slow == fast:
            break

    return slow == 1


s = 100
print(solution(s))
