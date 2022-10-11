"""
Бригада скорой помощи выехала по вызову в один из отделенных районов. К сожалению, когда диспетчер получил вызов, он успел записать только адрес дома и номер квартиры K1, а затем связь прервалась. Однако он вспомнил, что по этому же адресу дома некоторое время назад скорая помощь выезжала в квартиру K2, которая расположена в подъезда P2 на этаже N2. Известно, что в доме M этажей и количество квартир на каждой лестничной площадке одинаково. Напишите программу, которая вычилсяет номер подъезда P1 и номер этажа N1 квартиры K1.

Формат ввода
Во входном файле записаны пять положительных целых чисел K1, M, K2, P2, N2. Все числа не превосходят 106.

Формат вывода
Выведите два числа P1 и N1. Если входные данные не позволяют однозначно определить P1 или N1, вместо соответствующего числа напечатайте 0. Если входные данные противоречивы, напечатайте два числа –1 (минус один).
"""

import random


MAX_FLATS = 10000


def get_ent_and_floor(k, flats_on_floot, m):
    floors_before = (k - 1) // flats_on_floot
    ent = floors_before // m + 1
    floor = floors_before % m + 1
    return ent, floor


def check(k1, m, k2, p2, n2, flats_on_floor):
    ent2, floor2 = get_ent_and_floor(k2, flats_on_floor, m)
    if ent2 == p2 and floor2 == n2:
        return get_ent_and_floor(k1, flats_on_floor, m)
    return -1, -1


def slow(k1, m, k2, p2, n2):
    # подъезд
    ent = -1
    # этаж
    floor = -1
    # Флаг что нашли решение
    good_flag = False
    for flats_on_floor in range(1, MAX_FLATS):
        n_ent, n_floor = check(k1, m, k2, p2, n2, flats_on_floor)
        if n_ent != -1:
            good_flag = True
            if ent == -1:
                ent, floor = n_ent, n_floor
            else:
                if ent != n_ent and ent != 0:
                    ent = 0
                if floor != n_floor and floor != 0:
                    floor = 0
    if good_flag:
        return (ent, floor)
    else:
        return (-1, -1)


def fast(k1, m, k2, p2, n2):
    f2 = (p2 - 1) * m + n2
    if f2 == 1:
        if k1 <= k2:
            return (1, 1)
        elif m == 1:
            return (0, 1)
        elif (k1 - 1) // k2 + 1 <= m:
            return (1, 0)
        else:
            return (0, 0)
    else:
        # Минимальное количество квартир на этаже
        cnt_min = (k2 - 1) // f2 + 1
        # порядковый номер квартиры на этаже (от 1 до cnt_min)
        k_on_floor = (k2 - 1) % cnt_min + 1
        # сколько еще квартир с таким же номером поместиться на этаже n2
        cnt_yet = (k_on_floor - 1) // (f2 - 1)
        # максимальное количество квартир на этаже
        cnt_max = cnt_min + cnt_yet
        p1s = set()
        n1s = set()
        for cnt in range(cnt_min, cnt_max + 1):
            p1, n1 = check(k1, m, k2, p2, n2, cnt)
            if p1 == -1 or n1 == -1:
                return -1, -1
            else:
                p1s.add(p1)
                n1s.add(n1)

        p1_res = 0 if len(p1s) >= 2 else list(p1s)[0]
        p2_res = 0 if len(n1s) >= 2 else list(n1s)[0]

        return p1_res, p2_res


def my_test():
    max_rand_vals = 100
    while True:
        rand_vals = [random.randint(1, max_rand_vals) for _ in range(5)]
        k1, m, k2, p2, n2 = rand_vals
        slow_ans = slow(k1, m, k2, p2, n2)
        fast_ans = fast(k1, m, k2, p2, n2)
        print(*rand_vals)
        if slow_ans == fast_ans:
            print("OK")
        else:
            print(f"WA fast={fast_ans} slow={slow_ans}")
            break


def input_data():
    K1, M, K2, P2, N2 = [int(x) for x in input().split()]
    return K1, M, K2, P2, N2


def work():
    pass


if __name__ == "__main__":
    K1, M, K2, P2, N2 = input_data()
    res = slow(K1, M, K2, P2, N2)
    print(*res)
    # print(fast(3, 2, 1, 1, 1), slow(3, 2, 1, 1, 1))
    # my_test()
