"""
Некоторый банк хочет внедрить систему управления счетами клиентов, поддерживающую
следующие операции:
    * Пополнение счета клиента.
    * Снятие денег со счета.
    * Запрос остатка средств на счете.
    * Перевод денег между счетами клиентов.
    * Начисление процентов всем клиентам.

Вам необходимо реализовать такую систему. Клиенты банка идентифицируются именами
(уникальная строка, не содержащая пробелов). Первоначально у банка нет ни одного клиента.
Как только для клиента проводится операция пололнения, снятия или перевода денег,
ему заводится счет с нулевым балансом. Все дальнейшие операции проводятся только
с этим счетом. Сумма на счету может быть как положительной, так и отрицательной,
при этом всегда является целым числом.

Формат ввода
Входной файл содержит последовательность операций. Возможны следующие операции:
    * DEPOSIT name sum - зачислить сумму sum на счет клиента name. Если у клиента
нет счета, то счет создается.
    * WITHDRAW name sum - снять сумму sum со счета клиента name. Если у клиента нет
счета, то счет создается.
    * BALANCE name - узнать остаток средств на счету клиента name.
TRANSFER name1 name2 sum - перевести сумму sum со счета клиента name1 на счет клиента name2.
Если у какого-либо клиента нет счета, то ему создается счет.
    * INCOME p - начислить всем клиентам, у которых открыты счета, p% от суммы счета.
Проценты начисляются только клиентам с положительным остатком на счету, если у клиента
остаток отрицательный, то его счет не меняется.
    * После начисления процентов сумма на счету остается целой, то есть начисляется
только целое число денежных единиц.
Дробная часть начисленных процентов отбрасывается.

Формат вывода
Для каждого запроса BALANCE программа должна вывести остаток на счету данного клиента.
Если же у клиента с запрашиваемым именем не открыт счет в банке, выведите ERROR.

Пример 1
Ввод
DEPOSIT Ivanov 100
INCOME 5
BALANCE Ivanov
TRANSFER Ivanov Petrov 50
WITHDRAW Petrov 100
BALANCE Petrov
BALANCE Sidorov

Вывод
105
-50
ERROR


Пример 2
Ввод
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Ivanov 100
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Petrov 150
BALANCE Petrov
DEPOSIT Ivanov 10
DEPOSIT Petrov 15
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Ivanov 46
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Petrov 14
BALANCE Ivanov
BALANCE Petrov

Вывод
ERROR
ERROR
100
ERROR
150
110
165
156
165
156
179


Пример 3
Ввод
BALANCE a
BALANCE b
DEPOSIT a 100
BALANCE a
BALANCE b
WITHDRAW a 20
BALANCE a
BALANCE b
WITHDRAW b 78
BALANCE a
BALANCE b
WITHDRAW a 784
BALANCE a
BALANCE b
DEPOSIT b 849
BALANCE a
BALANCE b

Вывод
ERROR
ERROR
100
ERROR
80
ERROR
80
-78
-704
-78
-704
771
"""


from collections import defaultdict
import sys


def solve():
    bank = defaultdict(lambda: 0)
    ans = []
    for line in sys.stdin:
        oper, *data = line.split()
        if oper == "BALANCE":
            name = data[0]
            if name not in bank:
                ans.append("ERROR")
            else:
                ans.append(bank[name])
        elif oper == "DEPOSIT":
            name = data[0]
            s = int(data[1])
            bank[name] += s
        elif oper == "WITHDRAW":
            name = data[0]
            s = int(data[1])
            bank[name] -= s
        elif oper == "TRANSFER":
            name1 = data[0]
            name2 = data[1]
            s = int(data[2])
            bank[name1] -= s
            bank[name2] += s
        else:
            # Значит остаётся операция INCOME
            p = int(data[0])
            for name in bank:
                if bank[name] > 0:
                    bank[name] += bank[name]*p//100

    return ans


if __name__ == "__main__":
    res = solve()
    print(*res, sep="\n")
