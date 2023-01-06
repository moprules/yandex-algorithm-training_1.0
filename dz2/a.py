"""
A. Возрастает ли список?

Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли, что
каждый элемент этого списка больше предыдущего).

Выведите YES, если массив монотонно возрастает и NO в противном случае.
Пример 1
Ввод	Вывод
1 7 9   YES

Пример 2
Ввод	Вывод
1 9 7   NO

Пример 3
Ввод	Вывод
2 2 2   NO
"""


def input_data():
    return [int(x) for x in input().split()]


def isGrow(mas: list):
    for i in range(1, len(mas)):
        if mas[i] <= mas[i - 1]:
            return "NO"
    return "YES"


if __name__ == "__main__":
    mas = input_data()
    res = isGrow(mas)
    print(res)
