"""
Даны три натуральных числа. Возможно ли построить треугольник с такими сторонами. Если это возможно, выведите строку YES, иначе выведите строку NO.

Треугольник — это три точки, не лежащие на одной прямой.

Формат ввода
Вводятся три натуральных числа.

Формат вывода
Выведите ответ на задачу.
"""


def input_data():
    a = int(input())
    b = int(input())
    c = int(input())
    return sorted([a, b, c])


def get_answer(a, b, c):
    if a + b > c:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    a, b, c = input_data()
    print(get_answer(a, b, c))
