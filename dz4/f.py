"""
F. Продажи

Дана база данных о продажах некоторого интернет-магазина. Каждая строка входного
файла представляет собой запись вида Покупатель товар количество,
где Покупатель — имя покупателя (строка без пробелов),товар — название товара
(строка без пробелов), количество — количество приобретенных единиц товара.
Создайте список всех покупателей, а для каждого покупателя подсчитайте
количество приобретенных им единиц каждого вида товаров.

Формат ввода
Вводятся сведения о покупках в указанном формате.

Формат вывода
Выведите список всех покупателей в лексикографическом порядке, после имени
каждого покупателя выведите двоеточие, затем выведите список названий всех
приобретенных данным покупателем товаров в лексикографическом порядке, после
названия каждого товара выведите количество единиц товара, приобретенных данным
покупателем. Информация о каждом товаре выводится в отдельной строке.

Пример 1
Ввод
Ivanov paper 10
Petrov pens 5
Ivanov marker 3
Ivanov paper 7
Petrov envelope 20
Ivanov envelope 5
Вывод
Ivanov:
envelope 5
marker 3
paper 17
Petrov:
envelope 20
pens 5

Пример 2
Ввод
Ivanov aaa 1
Petrov aaa 2
Sidorov aaa 3
Ivanov aaa 6
Petrov aaa 7
Sidorov aaa 8
Ivanov bbb 3
Petrov bbb 7
Sidorov aaa 345
Ivanov ccc 45
Petrov ddd 34
Ziborov eee 234
Ivanov aaa 45
Вывод
Ivanov:
aaa 52
bbb 3
ccc 45
Petrov:
aaa 9
bbb 7
ddd 34
Sidorov:
aaa 356
Ziborov:
eee 234
"""


from collections import defaultdict
import sys


def solve():
    d = defaultdict(lambda: defaultdict(lambda: 0))
    for line in sys.stdin:
        name, product, cnt = line.split()
        d[name][product] += int(cnt)

    ans = []
    for name in sorted(d):
        ans.append(name+":")
        for prod in sorted(d[name]):
            ans.append(f'{prod} {d[name][prod]}')

    return ans


if __name__ == "__main__":
    res = solve()
    print(*res, sep="\n")
