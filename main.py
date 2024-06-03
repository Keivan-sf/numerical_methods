import math
from typing import Callable


def polynomial_2(n, x):
    if n == 0:
        return 4 * (x ** 2) + 200 * x + 12
    if n == 1:
        return 8 * x + 200
    if n == 2:
        return 8
    return 0


def polynomial_3(n, x):
    if n == 0:
        return 7 * (x ** 3) + 2 * (x ** 2) + 99*x + 4
    if n == 1:
        return 21 * (x ** 2) + 4 * x + 99
    if n == 2:
        return 42 * x + 4
    if n == 3:
        return 42
    return 0


def polynomial_4(n, x):
    if n == 0:
        return 3 * (x ** 4) + 100*x + 55
    if n == 1:
        return 12 * (x ** 3) + 100
    if n == 2:
        return 36 * (x ** 2)
    if n == 3:
        return 72 * x
    if n == 4:
        return 72
    return 0


def sin(n, x):
    if n % 4 == 0:
        return math.sin(x)
    if n % 4 == 1:
        return math.cos(x)
    if n % 4 == 2:
        return -math.sin(x)
    return -math.cos(x)


def cos(n, x):
    if n % 4 == 0:
        return math.cos(x)
    if n % 4 == 1:
        return -math.sin(x)
    if n % 4 == 2:
        return -math.cos(x)
    return math.sin(x)


def bisection(a: float, b: float, f: Callable[[float, float], float], iterations: int):
    """
        f(a) must be positive
        f(b) must be negative
    """
    c = a
    for _ in range(iterations):
        c = (a + b)/2
        fc = f(0, c)
        if fc > 0:
            a = c
        elif fc < 0:
            b = c
        else:
            return c
    return c


def regula_falsi(a: float, b: float, f: Callable[[float, float], float],  iterations: int):
    """
        f(a) must be positive
        f(b) must be negative
    """
    c = a
    for _ in range(iterations):
        fa = f(0, a)
        fb = f(0, b)
        c = (a*fb - b*fa) / (fb - fa)
        fc = f(0, c)
        if fc > 0:
            a = c
        elif fc < 0:
            b = c
        else:
            return c
    return c


def newton(x: float, f: Callable[[float, float], float],  iterations: int):
    for _ in range(iterations):
        x = x - (f(0, x) / f(1, x))
    return x


def secant(x1: float, x2: float, f: Callable[[float, float], float],  iterations: int):
    for _ in range(iterations):
        fx1 = f(0, x1)
        fx2 = f(0, x2)
        if x1 - x2 == 0 or fx1 - fx2 == 0:
            return x2
        temp = (x1 * fx2 - x2 * fx1) / (fx2 - fx1)
        x1 = x2
        x2 = temp
    return x2


def get_function_from_user() -> Callable[[float, float], float]:
    print("\nPlease select a function to continue:\n")
    print("1. 4x^2 + 200x + 12")
    print("2. 7x^3 + 2x^2 + 99x + 4")
    print("3. 3x^4 + 100x + 55")
    print("4. sin(x)")
    print("5. cos(x)")
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
            return sin
        if n == 5:
            return cos


f = get_function_from_user()
# c = bisection(1.2, 1.78, f, 200)
c1 = regula_falsi(1.2, 1.78, f, 20)
c2 = newton(1.2, f, 20)
c3 = secant(1.2, 1.78, f, 20)

print(c1, c2, c3, f(0, c1), f(0, c2), f(0, c3))
