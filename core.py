'''
Математическое ядро для алгоритма вычисления площади криволинейной трапеции.
Использует методы:
- Метод прямоугольниклов
    + Левый
    + Правый
    + Средний
- Метод Симпсона

Преддоставляет все необходимые функции и поля для вычисления площади криволинейной трапеции, включая:
- Вычисление площади по формуле прямоугольников
- Вычисление площади по формуле Симпсона
'''
import math
    

def step_dividing(a: float, b: float, n: float):
    h = (b - a) / n
    return h


def rectangle_left(f, a, b, n):
    h = step_dividing(a, b, n)
    s = 0.0
    x = a

    for _ in range(n):
        s += f(x)
        x += h

    return h * s


def rectangle_right(f, a, b, n):
    h = step_dividing(a, b, n)
    s = 0.0
    x = a + h

    for _ in range(n):
        s += f(x)
        x += h

    return h * s


def rectangle_mid(f, a, b, n):
    h = step_dividing(a, b, n)
    s = 0.0
    x = a + 0.5 * h

    for _ in range(n):
        s += f(x)
        x += h

    return h * s


def simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n должно быть четным")

    h = step_dividing(a, b, n)
    s = f(a) + f(b)

    x = a + h

    for i in range(1, n):
        s += 4*f(x) if i % 2 else 2*f(x)
        x += h

    return (h / 3) * s