"""
E. OpenCalculator

В новой программе OpenCalculator появилась новая возможность – можно настроить,
какие кнопки отображаются, а какие – нет. Если кнопка не отображается на экране,
то ввести соответствующую цифру с клавиатуры или копированием из другой программы
нельзя. Петя настроил калькулятор так, что он отображает только кнопки с цифрами x, y, z.
Напишите программу, определяющую, сможет ли Петя ввести число N, а если нет,
то какое минимальное количество кнопок надо дополнительно отобразить на экране для его ввода.

Формат ввода
Сначала вводятся три различных числа из диапазона от 0 до 9: x, y и z
(числа разделяются пробелами). Далее вводится целое неотрицательное
число N, которое Петя хочет ввести в калькулятор. Число N не превышает 10000.

Формат вывода
Выведите, какое минимальное количество кнопок должно быть добавлено для того,
чтобы можно было ввести число N (если число может быть введено с помощью уже
имеющихся кнопок, выведите 0)

Пример 1
Ввод
1 2 3
1123
Вывод
0

Пример 2
Ввод
1 2 3
1001
Вывод
1

Пример 3
Ввод
5 7 3
123
Вывод
2
"""


def work():
    xyz = set(input().split())
    user_num = set(input())
    # нужные клавиши - разность множеств
    need_keys = user_num - xyz
    return len(need_keys)


if __name__ == "__main__":
    res = work()
    print(res)
