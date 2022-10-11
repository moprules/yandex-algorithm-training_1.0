"""
В данном списке из n ≤ 105 целых чисел найдите три числа,произведение которых максимально.

Решение должно иметь сложность O(n), где n - размер списка.

Выведите три искомых числа в любом порядке.

Пример 1
Ввод
3 5 1 7 9 0 9 -3 10
Вывод
10 9 9

Пример 2
Ввод
-5 -30000 -12
Вывод
-5 -12 -30000

Пример 3
Ввод
1 2 3
Вывод
3 2 1
"""


from argparse import ArgumentError


def input_data():
    nums = [int(x) for x in input().split()]
    return nums


def mult(mas):
    if not mas:
        raise ArgumentError
    else:
        m = 1
        for x in mas:
            m *= x
        return m


def work(nums: list):
    # Минимальные отрицательные числа
    min_m = [None, None]
    # Максимальные отрицательные числа
    max_m = [None, None, None]
    # Минимальные положительные числа
    min_p = [None, None]
    # Максимальные положительные числа
    max_p = [None, None, None]

    for num in nums:
        if num < 0:
            if min_m[0] is None or min_m[0] > num:
                min_m[1] = min_m[0]
                min_m[0] = num
            elif min_m[1] is None or min_m[1] > num:
                min_m[1] = num

            if max_m[0] is None or max_m[0] < num:
                max_m[2] = max_m[1]
                max_m[1] = max_m[0]
                max_m[0] = num
            elif max_m[1] is None or max_m[1] < num:
                max_m[2] = max_m[1]
                max_m[1] = num
            elif max_m[2] is None or max_m[2] < num:
                max_m[2] = num
        else:
            if min_p[0] is None or min_p[0] > num:
                min_p[1] = min_p[0]
                min_p[0] = num
            elif min_p[1] is None or min_p[1] > num:
                min_p[1] = num

            if max_p[0] is None or max_p[0] < num:
                max_p[2] = max_p[1]
                max_p[1] = max_p[0]
                max_p[0] = num
            elif max_p[1] is None or max_p[1] < num:
                max_p[2] = max_p[1]
                max_p[1] = num
            elif max_p[2] is None or max_p[2] < num:
                max_p[2] = num

    vers_trash = [max_m, max_p, (*min_m, max_p[0]), (max_m[0], *min_p)]
    vers = []
    for ver in vers_trash:
        if None not in ver:
            vers.append(ver)

    max_ver = vers[0]
    max_mult = mult(max_ver)
    for i in range(1, len(vers)):
        cur_mult = mult(vers[i])
        if cur_mult > max_mult:
            max_mult = cur_mult
            max_ver = vers[i]

    return max_ver


if __name__ == "__main__":
    nums = input_data()
    res = work(nums)
    print(*res)
