import math
from typing import Callable


def polynomial_2(x):
    return 4 * (x ** 2) + 200 * x + 12


def polynomial_3(x):
    return 7 * (x ** 3) + 99*x + 4


def polynomial_4(x):
    return 3 * (x ** 4) + 100*x + 55


def bisection(a: float, b: float, f: Callable[[float], float], iterations: int):
    """
        f(a) must be positive
        f(b) must be negative
    """
    c = a
    for _ in range(iterations):
        c = (a + b)/2
        fc = f(c)
        if fc > 0:
            a = c
        elif fc < 0:
            b = c
        else:
            return c
    return c


def regula_falsi(a: float, b: float, f: Callable[[float], float],  iterations: int):
    """
        f(a) must be positive
        f(b) must be negative
    """
    c = a
    for _ in range(iterations):
        fa = f(a)
        fb = f(b)
        c = (a*fb - b*fa) / (fb - fa)
        fc = f(c)
        if fc > 0:
            a = c
        elif fc < 0:
            b = c
        else:
            return c
    return c


def get_function_from_user() -> Callable[[float], float]:
    print("\nPlease select a function to continue:\n")
    print("1. 4x^2 + 200x + 12")
    print("2. 7x^3 + 99x + 4")
    print("3. 3x^4 + 100x + 55")
    print("4. sin(x)")
    print("5. cos(x)")
    print("6. tan(x)")
    print("7. cosh(x)")
    print("8. sinh(x)")
    while (True):
        n = int(input("-> "))
        if n > 11 or n < 1:
            print("wrong input, please try again")
            continue
        if n == 1:
            return polynomial_2
        if n == 2:
            return polynomial_3
        if n == 3:
            return polynomial_4
        if n == 4:
            return math.sin
        if n == 5:
            return math.cos
        if n == 6:
            return math.tan
        if n == 7:
            return math.cosh
        if n == 9:
            return math.sinh
        if n == 10:
            return math.asin
        if n == 11:
            return math.acos


f = get_function_from_user()
print(bisection(1, -1, f, 40))
print(regula_falsi(1, -1, f, 30))
