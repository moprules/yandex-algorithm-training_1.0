"""
G. Наибольшее произведение двух чисел

Дан список, заполненный произвольными целыми числами. Найдите в этом списке два числа,
произведение которых максимально. Выведите эти числа в порядке неубывания.

Список содержит не менее двух элементов. Числа подобраны так, что ответ однозначен.

Решение должно иметь сложность O(n), где n - размер списка.

Пример 1
Ввод	     Вывод
4 3 5 2 5    5 5

Пример 2
Ввод	     Вывод
-4 3 -5 2 5  -5 -4

Пример 3
Ввод
12288 -10075 29710 15686 -18900 -17715 15992 24431 6220 28403 -23148 18480 -22905 5411 -7602 15560 -26674 11109 -4323 6146 -1523 4312 10666 -15343 -17679 7284 20709 -7103 24305 14334 -12281 17314 26061 25616 17453 16618 -24230 -19788 21172 11339 2202 -22442 -20997 1879 -8773 -8736 5310 -23372 12621 -25596 -28609 -13309 -13 10336 15812 -21193 21576 -1897 -12311 -6988 -25143 -3501 23231 26610 12618 25834 -29140 21011 23427 1494 15215 23013 -15739 8325 5359 -12932 18111 -72 -12509 20116 24390 1920 17487 25536 24934 -6784 -16417 -2222 -16569 -25594 4491 14249 -28927 27281 3297 5998 6259 4577 12415 3779 -8856 3994 19941 11047 2866 -24443 -17299 -9556 12244 6376 -13694 -14647 -22225 21872 7543 -6935 17736 -2464 9390 1133 18202 -9733 -26011 13474 29793 -26628 -26124 27776 970 14277 -23213 775 -9318 29014 -5645 -27027 -21822 -17450 -5 -655 22807 -20981 16310 27605 -18393 914 7323 599 -12503 -28684 5835 -5627 25891 -11801 21243 -21506 22542 -5097 8115 178 10427 25808 10836 -11213 18488 21293 14652 12260 42 21034 8396 -27956 13670 -296 -757 18076 -15597 4135 -25222 -19603 8007 6012 2704 28935 16188 -20848 13502 -11950 -24466 5440 26348 27378 7990 -11523 -26393 
Вывод
29710 29793
"""
from math import prod


def input_data():
    nums = [int(x) for x in input().split()]
    return nums


def work(nums: list):
    # Положительные максимумы в массиве
    mp1 = mp2 = None
    # Отрицательные максимумы в массиве
    mm1 = mm2 = None
    for num in nums:
        if num < 0:
            if mm1 is None or num < mm1:
                mm2 = mm1
                mm1 = num
            elif mm2 is None or num < mm2:
                mm2 = num
        else:
            if mp2 is None or mp2 < num:
                mp1 = mp2
                mp2 = num
            elif mp1 is None or mp1 < num:
                mp1 = num
    # Есть три возможных варианты ответа
    # 1 - два положтельных максимума
    # 2 - два отрицательных максимума (по модулю)
    # 3 - один отрицательный максимум(по модулю), один положительный максимум
    variants = [(mp1, mp2), (mm1, mm2), (mm1, mp2)]
    # Если где-то содержится None по умолчанию, то такого варианта нет
    variants = [v for v in variants if None not in v]
    # По условию задачи ответ однозначен, значит variants не может быть пустым
    # Список произведений чисел
    mults = [prod(v) for v in variants]
    # Ищем пару чисел с максимальным произведением
    i_max = 0
    for i in range(1, len(mults)):
        if mults[i_max] < mults[i]:
            i_max = i
    return variants[i_max]


if __name__ == "__main__":
    nums = input_data()
    res = work(nums)
    print(*res)
