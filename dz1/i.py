"""
За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D x E. Замок Иф сложен из кирпичей, размером A x B x C. Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие, если стороны кирпича должны быть параллельны сторонам отверстия.

Формат ввода
Программа получает на вход числа A, B, C, D, E.

Формат вывода
Программа должна вывести слово YES или NO.
"""


def input_data():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    return a, b, c, d, e


def work(a, b, c, d, e):
    a, b, c = sorted([a, b, c])
    d, e = sorted([d, e])
    if a <= d and b <= e:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    a, b, c, d, e = input_data()
    res = work(a, b, c, d, e)
    print(res)
