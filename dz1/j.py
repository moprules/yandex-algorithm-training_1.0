"""
Даны числа a, b, c, d, e, f. Решите систему линейных уравнений
a*x + b*y = e
c*x + d*y = f
Формат ввода
Вводятся 6 вещественных чисел - коэффициенты уравнений.

Формат вывода
Вывод программы зависит от вида решения этой системы. Если система не имеет решений, то программа должна вывести единственное число 0. Если система имеет бесконечно много решений, каждое из которых имеет вид y=kx+b, то программа должна вывести число 1, а затем значения k и b. Если система имеет единственное решение (x0,y0), то программа должна вывести число 2, а затем значения x0 и y0. Если система имеет бесконечно много решений вида x=x0, y — любое, то программа должна вывести число 3, а затем значение x0. Если система имеет бесконечно много решений вида y=y0, x — любое, то программа должна вывести число 4, а затем значение y0. Если любая пара чисел (x,y) является решением, то программа должна вывести число 5.

Числа x0 и y0 будут проверяться с точностью до пяти знаков после точки.
"""

import random


def input_data():
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    f = float(input())

    return a, b, c, d, e, f


def det(a, b, c, d):
    return a * d - c * b


def work(a, b, c, d, e, f):
    if (b != 0 and d != 0 and (b + d) == 0) or (a != 0 and c != 0 and (a + c) == 0):
        b *= -1
        a *= -1
        e *= -1
    # определитель всей системы
    det_com = det(a, b, c, d)
    d1 = det(e, b, f, d)
    d2 = det(a, e, c, f)
    # если он не равен 0
    if det_com != 0:
        # система однозначно решается
        x0 = f"{d1 / det_com:.5f}"
        y0 = f"{d2 / det_com:.5f}"
        return [2, x0, y0]
    elif [d1, d2].count(0) < 2:
        # нет решений
        return [0]
    else:
        # бесконечно много решений
        if a == b == c == d == e == f == 0:
            return [5]
        elif a == b == c == d == 0:
            return [0]
        elif a == c == 0:
            y0 = f"{(e+f) / (b+d):.5f}"
            return [4, y0]
        elif b == d == 0:
            x0 = f"{(e+f) / (a+c):.5f}"
            return [3, x0]
        else:
            k0 = -((a + c) / (b + d))
            k0 = f"{k0:.5f}"
            b0 = (e + f) / (b + d)
            b0 = f"{b0:.5f}"
            return [1, k0, b0]


def my_test():
    max_val = 3
    while True:
        a, b, c, d, e, f = [random.randint(-max_val, max_val) for _ in range(6)]
        print(a, b, c, d, e, f)
        res = work(a, b, c, d, e, f)
        if res:
            print("OK")
        else:
            print("NO")
            break


if __name__ == "__main__":
    a, b, c, d, e, f = input_data()
    res = work(a, b, c, d, e, f)
    print(*res)
    # my_test()
    # res = work(0, 0, 0, 0, 1, 1)
    # print(res)
