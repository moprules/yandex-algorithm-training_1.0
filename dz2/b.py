"""
B. Определить вид последовательности

По последовательности чисел во входных данных определите ее вид:

CONSTANT – последовательность состоит из одинаковых значений
ASCENDING – последовательность является строго возрастающей
WEAKLY ASCENDING – последовательность является нестрого возрастающей
DESCENDING – последовательность является строго убывающей
WEAKLY DESCENDING – последовательность является нестрого убывающей
RANDOM – последовательность не принадлежит ни к одному из вышеупомянутых типов
Формат ввода
По одному на строке поступают числа последовательности ai, |ai| <= 10^9.

Признаком окончания последовательности является число -2*10^9. Оно в последовательность не входит.

Формат вывода
В единственной строке выведите тип последовательности.

Ввод	             Вывод
-530                 CONSTANT
-530
-530
-530
-530
-530
-2000000000
"""


def input_data():
    mas = []
    while True:
        x = float(input())
        if x == -2000000000:
            return mas
        else:
            mas.append(x)


def work(mas: list):
    if len(mas) == 1:
        return "CONSTANT"

    who = set()
    for i in range(1, len(mas)):
        before = mas[i - 1]
        x = mas[i]
        if x == before:
            who.add("CONSTANT")
        elif x > before:
            who.add("ASCENDING")
        elif x < before:
            who.add("DESCENDING")

    if len(who) == 1:
        return list(who)[0]
    elif "ASCENDING" in who and "DESCENDING" in who:
        return "RANDOM"
    else:
        base = list(who - {"CONSTANT"})[0]
        return f"WEAKLY {base}"


if __name__ == "__main__":
    mas = input_data()
    res = work(mas)
    print(res)
