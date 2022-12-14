"""
A. Стильная одежда

Глеб обожает шоппинг. Как-то раз он загорелся идеей подобрать себе майку
и штаны так, чтобы выглядеть в них максимально стильно. В понимании Глеба
стильность одежды тем больше, чем меньше разница в цвете элементов его одежды.

В наличии имеется N (1 <= N <= 100000) маек и M (1 <= M <= 100000) штанов,
про каждый элемент известен его цвет (целое число от 1 до 10000000).
Помогите Глебу выбрать одну майку и одни штаны так,
чтобы разница в их цветебыла как можно меньше.

Формат ввода
Сначала вводится информация о майках:
    в первой строке целое число N (1 <= N <= 100000) и
    во второй N целых чисел от 1 до 10000000 — цвета имеющихся в наличии маек.
    Гарантируется, что номера цветов идут в возрастающем порядке
    (в частности, цвета никаких двух маек не совпадают).
Далее в том же формате идёт описание штанов: их количество M (1 <= M <= 100000)
    и в следующей строке M целых чисел от 1 до 10000000 в возрастающем
    порядке — цвета штанов.

Формат вывода
Выведите пару неотрицательных чисел — цвет майки и цвет штанов,
которые следует выбрать Глебу. Если вариантов выбора несколько,
выведите любой из них.

Пример 1
Ввод
2
3 4
3
1 2 3
Вывод
3 3

Пример 2
Ввод
2
4 5
3
1 2 3
Вывод
4 3

Пример 3
Ввод
5
1 2 3 4 5
5
1 2 3 4 5
Вывод
1 1

"""


def input_data():
    n = int(input())
    mas1 = [int(num) for num in input().split()]
    m = int(input())
    mas2 = [int(num) for num in input().split()]
    return n, mas1, m, mas2


def solve(n, mas1, m, mas2):
    i1 = 0
    i2 = 0
    i1_best = 0
    i2_best = 0
    style_best = abs(mas1[i1_best] - mas2[i2_best])

    while i1 < n and i2 < m:
        if mas1[i1] == mas2[i2]:
            return mas1[i1], mas2[i2]

        style = abs(mas1[i1] - mas2[i2])

        if style < style_best:
            i1_best = i1
            i2_best = i2
            style_best = style

        if mas1[i1] < mas2[i2]:
            i1 += 1
        else:
            i2 += 1

    return mas1[i1_best], mas2[i2_best]


if __name__ == "__main__":
    n, mas1, m, mas2 = input_data()
    res = solve(n, mas1, m, mas2)
    print(*res)
