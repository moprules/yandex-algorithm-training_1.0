"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей и выведите количество таких элементов.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода
Выведите ответ на задачу.

Пример 1
Ввод	    Вывод
1 2 3 4 5   0

Пример 2
Ввод	    Вывод
5 4 3 2 1   0

Пример 3
Ввод	    Вывод
1 5 1 5 1   2
"""


def input_data():
    return [int(x) for x in input().split()]


def work(nums: list):
    if len(nums) < 3:
        return 0
    cnt = 0
    for i in range(1, len(nums) - 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            cnt += 1
    return cnt


if __name__ == "__main__":
    nums = input_data()
    res = work(nums)
    print(res)
