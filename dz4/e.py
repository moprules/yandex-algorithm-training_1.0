"""
Для строительство двухмерной пирамиды используются прямоугольные блоки,
каждый из которых характеризуется шириной и высотой. Можно поставить
один блок на другой, только если ширина верхнего блока строго меньше
ширины нижнего. Самым нижним в пирамиде может быть блок любой ширины.
По заданному набору блоков определите, пирамиду какой наибольшей высоты
можно построить из них.

Формат ввода
В первой строке входных данных задается число N — количество блоков (
1 ≤ N ≤100000).
В следующих N строках задаются пары натуральных чисел wi и hi (1 ≤ wi, hi≤10^9)
— ширина и высота блока соответственно.

Формат вывода
Выведите одно целое число — максимальную высоту пирамиды.

Пример
Ввод
3
3 1
2 2
3 3
Вывод
5

Примечания
В примере пирамида будет состоять из двух блоков: нижним блоком будет блок номер 3,
а верхним — блок номер 2. Блок номер 1 нельзя использовать вместе с блоком номер 3.
"""


from collections import defaultdict


def solve():
    n = int(input())
    d = defaultdict(lambda: 0)
    for _ in range(n):
        w, h = map(int, input().split())
        d[w] = max(d[w], h)

    h = 0
    for w in d:
        h += d[w]

    return h


if __name__ == "__main__":
    res = solve()
    print(res)