import math
import numpy.polynomial.polynomial as np
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


def lagrange(x: list[float], f: list[float], n: int):
    sum = np.polymul((0), (0))
    for i in range(n):
        numerator = np.polymul((1), (1))
        denominator = 1
        for j in range(n):
            if i == j:
                continue
            numerator = np.polymul((1, -x[j]), numerator)
            denominator *= (x[i] - x[j])
        Li = np.polymul(numerator, 1 / denominator)
        Li_fi = np.polymul(Li, f[i])
        sum = np.polyadd(sum, Li_fi)
    return sum


def polynomial_to_str(p):
    n = len(p)
    s = ""
    j = 0
    for i in p:
        j += 1
        I = round(i)
        if I == 0:
            continue
        sign = ' + ' if I > 0 else ' - '
        I = abs(I)
        s += sign
        s += (str(I) if I > 1 or n - j == 0 else "")
        s += ("x" if n - j > 0 else "")
        s += ("" if n - j <= 1 else "^" + str(n - j))
    s = s[3:]
    return s


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


def get_function_data_from_user() -> tuple[list[float], list[float], int]:
    n = int(input("Enter the number of points you want to give: "))

    print("\nEnter all X values separated via space, for example: 1.2 4 -11.4 1.5 ...")
    while True:
        x = [float(i) for i in input().split()]
        if len(x) != n:
            print("you have to enter exactly", n,
                  "numbers since you have set it, please try again:")
            continue
        break

    print("\nEnter all Y values separated via space, for example: 1.7 5 22 1.52 ...")
    while True:
        y = [float(i) for i in input().split()]
        if len(y) != n:
            print("you have to enter exactly", n,
                  "numbers since you have set it, please try again:")
            continue
        break

    return x, y, n


def box_str(s: str):
    n = len(s)
    res = []
    res.append("+"*(n+8))
    res.append("+" + " "*(n+6) + "+")
    res.append("+   " + s + "   +")
    res.append("+" + " "*(n+6) + "+")
    res.append("+"*(n+8))
    return '\n'.join(res)


def main():
    while True:
        print("1. Bisection")
        print("2. Regula Falsi")
        print("3. Newton")
        print("4. Secant")
        print("5. Lagrange (linear interpolation)")
        print("0. Exit")
        n = int(input("\nPlease choose an option: "))

        while n > 5 or n < 0:
            n = int(input("wrong input! please try again: "))

        if n == 0:
            return

        if n == 1:
            f = get_function_from_user()
            a = float(input("\nEnter a: "))
            b = float(input("\nEnter b: "))
            while True:
                if (f(0, b) * f(0, a) >= 0):
                    print("f(b) * f(a) must be negative, please try again\n")
                    a = float(input("\nEnter a: "))
                    b = float(input("\nEnter b: "))
                    continue
                break
            if f(0, a) < 0 or f(0, b) > 0:
                a, b = b, a
            iterations = int(input(
                "Enter the number of iterations you want the program to perform (more than 0): "))
            output = str(bisection(a, b, f, iterations))
            print("\n\n" + box_str(output) + "\n\n")

        elif n == 2:
            f = get_function_from_user()
            a = float(input("\nEnter a: "))
            b = float(input("\nEnter b: "))
            while True:
                if (f(0, b) * f(0, a) >= 0):
                    print("f(b) * f(a) must be negative, please try again\n")
                    a = float(input("\nEnter a: "))
                    b = float(input("\nEnter b: "))
                    continue
                break
            if f(0, a) < 0 or f(0, b) > 0:
                a, b = b, a
            iterations = int(input(
                "Enter the number of iterations you want the program to perform (more than 0): "))
            output = str(regula_falsi(a, b, f, iterations))
            print("\n\n" + box_str(output) + "\n\n")

        elif n == 3:
            f = get_function_from_user()
            x = float(input("\nEnter x: "))
            iterations = int(input(
                "Enter the number of iterations you want the program to perform (more than 0): "))
            output = str(newton(x, f, iterations))
            print("\n\n" + box_str(output) + "\n\n")

        elif n == 4:
            f = get_function_from_user()
            x1 = float(input("\nEnter x1: "))
            x2 = float(input("\nEnter x2: "))
            iterations = int(input(
                "Enter the number of iterations you want the program to perform (more than 0): "))
            output = str(secant(x1, x2, f, iterations))
            print("\n\n" + box_str(output) + "\n\n")

        elif n == 5:
            print("")
            x, y, n = get_function_data_from_user()
            polynomial_res = lagrange(x, y, n)
            human_readable = polynomial_to_str(polynomial_res)
            print("\n\n" + box_str(human_readable) + "\n\n")


main()
