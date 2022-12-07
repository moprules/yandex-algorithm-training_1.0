"""
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу.

Пример 1
Ввод
apple orange banana banana orange
Вывод
banana

Пример 2
Ввод
oh you touch my tralala mmm my ding ding dong
Вывод
ding

Пример 3
Ввод
q w e r t y u i o p
a s d f g h j k l
z x c v b n m
Вывод
a
"""


from collections import defaultdict
import sys


def solve():
    d = defaultdict(lambda: 0)
    ans = ""
    for line in sys.stdin:
        for word in line.split():
            d[word] += 1
            if d[ans] < d[word] or (d[ans] == d[word] and word < ans):
                ans = word
    return ans


if __name__ == "__main__":
    res = solve()
    print(res)
