"""
Вам необходимо построить поле для игры "Сапер" по его конфигурации – размерам
и координатам расставленных на нем мин.

Вкратце напомним правила построения поля для игры "Сапер":
Поле состоит из клеток с минами и пустых клеток
Клетки с миной обозначаются символом *. Пустые клетки содержат число k_i,j такое,
что 0 <= k_i,j <= 8 – количество мин на соседних клетках.
Соседними клетками являются восемь клеток, имеющих смежный угол или сторону.

Формат ввода
В первой строке содержатся три числа: N, 1 ≤ N ≤ 100 - количество строк на поле,
M, 1 ≤ M ≤ 100 - количество столбцов на поле, K, 0 ≤ K ≤ N ⋅ M - количество мин на поле.
В следующих K строках содержатся по два числа с координатами мин:
p, 1 ≤ p ≤ N - номер строки мины, q, 1 ≤ 1 ≤ M - номер столбца мины.

Формат вывода
Выведите построенное поле, разделяя строки поля переводом строки, а столбцы - пробелом.

Пример 1
Ввод
3 2 2
1 1
2 2
Вывод
* 2
2 *
1 1

Пример 2
Ввод
2 2 0
Вывод
0 0
0 0

Пример 3
Ввод
4 4 4
1 3
2 1
4 2
4 4
Вывод
1 2 * 1 
* 2 1 1 
2 2 2 1 
1 * 2 * 
"""

from collections import defaultdict


def input_data():
    rows, cols, mines_cnt = [int(x) for x in input().split()]
    mines = []
    for _ in range(mines_cnt):
        x, y = [int(z) - 1 for z in input().split()]
        mines.append((x, y))
    return rows, cols, mines


def work(rows: int, cols: int, mines: list[tuple]):
    field = defaultdict(lambda: 0)
    for (x, y) in mines:
        field[x - 1, y - 1] += 1
        field[x, y - 1] += 1
        field[x + 1, y - 1] += 1

        field[x - 1, y] += 1
        field[x + 1, y] += 1

        field[x - 1, y + 1] += 1
        field[x, y + 1] += 1
        field[x + 1, y + 1] += 1

    for (x, y) in mines:
        field[x, y] = "*"

    return field


def print_field(rows: int, cols: int, field):
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(field[i, j])
        print(*row)


if __name__ == "__main__":
    rows, cols, mines = input_data()
    field = work(rows, cols, mines)
    print_field(rows, cols, field)
