"""
G. Счет в гипершашках

Андрей работает судьей на чемпионате по гипершашкам. В каждой игре в гипершашки
участвует три игрока. По ходу игры каждый из игроков набирает некоторое
положительное целое число баллов. Если после окончания игры первый игрок набрал
"a" баллов, второй — "b", а третий "c", то говорят, что игра закончилась со
счетом a:b:c.

Андрей знает, что правила игры гипершашек устроены таким образом,
что в результате игры баллы любых двух игроков различаются не более чем в k раз.

После матча Андрей показывает его результат, размещая три карточки с очками
игроков на специальном табло. Для этого у него есть набор из n карточек,
на которых написаны числа x1, x2, …, xn. Чтобы выяснить, насколько он готов
к чемпионату, Андрей хочет понять, сколько различных вариантов счета он сможет
показать на табло, используя имеющиеся карточки.

Требуется написать программу, которая по числу k и значениям чисел на карточках,
которые имеются у Андрея, определяет количество различных вариантов счета,
которые Андрей может показать на табло.

Формат ввода
Первая строка входного файла содержит два целых числа: n и k
(3 <= n <= 100000, 1 <= k <= 10^9).

Вторая строка входного файла содержит n целых чисел:
x1, x2, ..., xn (1 <= xi <= 10^9).

Формат вывода
Выходной файл должен содержать одно целое число
— искомое количество различных вариантов счета.

Пример
Ввод
5 2
1 1 2 2 3
Вывод
9

Примечания
В приведенном примере Андрей сможет показать следующие варианты счета:
1:1:2, 1:2:1, 2:1:1, 1:2:2, 2:1:2, 2:2:1, 2:2:3, 2:3:2, 3:2:2.
Другие тройки чисел, которые можно составить с использованием имеющихся
карточек, не удовлетворяют заданному условию, что баллы любых двух игроков
различаются не более чем в k = 2 раза.
"""


def input_data():
    n, k = map(int, input().split())
    x = [int(num) for num in input().split()]
    return n, x, k


def solve(n, x, k):
    # словарик для подсчёта карточек
    cards = {}
    for xi in x:
        if xi not in cards:
            cards[xi] = 0
        cards[xi] += 1
    # отсортированный массив уникальных карточек
    uniqs = sorted(cards)
    # указатель на правый элемент в массиве уникальных карточек
    right = 0
    # количество номеров с дубликатами
    duplicates = 0
    # переменная для результата
    # изначально считаем, что у нас 0 комбинаций карточек
    ans = 0
    # перебираем левый указатель
    for left in range(len(uniqs)):
        # двигаем правый указатель пока не выйдем за пределы массива
        # или не найдём карточку, которая
        while right < len(uniqs) and uniqs[left]*k >= uniqs[right]:
            # если количество карточек с данным номером больше одной
            if cards[uniqs[right]] > 1:
                # увеличиваем количество дубликатов
                duplicates += 1
            right += 1

        # расстояние между левым и правым указателем
        len_range = right - left

        if cards[uniqs[left]] >= 2:
            # две карточки с позиции left + все остальные подходящие
            ans += (len_range - 1) * 3
        if cards[uniqs[left]] >= 3:
            # все три картчки с позиции left
            ans += 1
        # каждая карточка уникальная
        ans += (len_range - 1) * (len_range - 2) * 3
        # Если карточек на позиции left > 1
        if cards[uniqs[left]] > 1:
            # нужно уменьшить счётчик дубликатов
            # так как на следующей итерации указатель left сместиться
            # и для учёта случая ниже
            duplicates -= 1
        # Случай когда одная карточка на позиции left + дубликаты
        ans += duplicates * 3

    return ans


if __name__ == "__main__":
    n, x, k = input_data()
    res = solve(n, x, k)
    print(res)
