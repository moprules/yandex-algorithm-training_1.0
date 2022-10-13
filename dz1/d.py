"""
Решите в целых числах уравнение:
sqrt(ax + b) = c

a, b, c – данные целые числа: найдите все решения или сообщите,
что решений в целых числах нет.
"""


def input_data():
    a = int(input())
    b = int(input())
    c = int(input())
    return a, b, c


def work(a, b, c):
    if c < 0:
        res = "NO SOLUTION"
    elif a == 0:
        if b == c**2:
            res = "MANY SOLUTIONS"
        else:
            res = "NO SOLUTION"
    else:
        # есть только одно решение
        x = (c**2 - b) / a
        if int(x) == x:
            res = int(x)
        else:
            res = "NO SOLUTION"

    return res


if __name__ == "__main__":
    a, b, c = input_data()
    print(work(a, b, c))
    # assert work(1, 0, 0) == 0
    # assert work(1, 2, 3) == 7
    # assert work(1, 2, -3) == "NO SOLUTION"
    # assert work(0, 0, 0) == "MANY SOLUTIONS"
    # assert work(1, -3, 0) == 3
