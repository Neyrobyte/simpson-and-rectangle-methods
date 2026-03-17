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
    

def step_dividing(a: int, b: int, n: int):
    h = (b - a) / n
    return h


def rectangle_left(f, a, b, n):
    # S = h * (y0 + y1 + ... + y(n-1))
    h = step_dividing(a, b, n)
    return h * sum(f(a + i*h) for i in range(n))


def rectangle_right(f, a, b, n):
    # S = h * (y1 + y2 + ... + yn)
    h = step_dividing(a, b, n)
    return h * sum(f(a + i*h) for i in range(1, n+1))


def rectangle_mid(f: callable, a, b, n):
    # S = h * (y0.5 + y1.5 + ... + y(n-0.5))
    h = step_dividing(a, b, n) / 3
    return h * sum(f(a + (i + 0.5)*h) for i in range(n))


def simpson(f, a, b, n):
    # S = (h / 3) * (y0 + yn + 2(y2 + y4 + ... + y(n-2)) + 4(y1 + y3 + ... + y(n-1)))
    if n % 2 != 0:
        return "N – должно быть четным для метода Симпсона."
    h = step_dividing(a, b, n) / 3
    s  = f(a) + f(b)
    
    for i in range(1, n):
        x = a + i*h
        s += 4*f(x) if i % 2 else 2*f(x)
    return s * h