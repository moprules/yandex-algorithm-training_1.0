"""
C. Кубики

Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор 
в каждом наборе все кубики различны по цвету. Однажды дети заинтересовались,
сколько существуют цветов таких, что кубики каждого цвета присутствуют в обоих
наборах. Для этого они занумеровали все цвета случайными числами. На этом их
энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части. Номер
любого цвета — это целое число в пределах от 0 до 10^9.

Формат ввода
В первой строке входного файла записаны числа N и M — количество кубиков у Ани
и Бори соответственно. В следующих N строках заданы номера цветов кубиков Ани.
В последних M строках номера цветов кубиков Бори.

Формат вывода
Выведите сначала количество, а затем отсортированные по возрастанию номера цветов
таких, что кубики каждого цвета есть в обоих наборах, затем количество и отсортированные
по возрастанию номера остальных цветов у Ани, потом количество и отсортированные
по возрастанию номера остальных цветов у Бори.

Пример 1
Ввод
4 3
0
1
10
9
1
3
0
Вывод
2
0 1
2
9 10
1
3

Пример 2
Ввод
2 2
1
2
2
3
Вывод
1
2
1
1
1
3

Пример 3
Ввод
0 0
Вывод
0

0

0
"""


def work():
    n, m = map(int, input().split())
    anya = {int(input()) for _ in range(n)}
    intersec = set()
    borya = set()
    for _ in range(m):
        x = int(input())
        if x in anya:
            intersec.add(x)
            anya.discard(x)
        else:
            borya.add(x)

    print(len(intersec))
    print(*sorted(intersec))
    print(len(anya))
    print(*sorted(anya))
    print(len(borya))
    print(*sorted(borya))


if __name__ == "__main__":
    work()
