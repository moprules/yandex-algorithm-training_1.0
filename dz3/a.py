"""
A. Количество различных чисел

Дан список чисел, который может содержать до 100000 чисел.
Определите, сколько в нем встречается различных чисел.

Формат ввода
Вводится список целых чисел. Все числа списка находятся на одной строке.
"""


def work():
    my_set = set(str_num for str_num in input().split())
    return len(my_set)


if __name__ == "__main__":
    res = work()
    print(res)
