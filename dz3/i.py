"""
I. Полиглоты

Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки
знают все школьники и языки, которые знает хотя бы один из школьников.

Формат ввода
Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi,
после каждого из чисел идет Mi строк, содержащих названия языков, которые знает
i-й школьник. Длина названий языков не превышает 1000 символов, количество различных
языков не более 1000. 1 <= N <= 1000, 1 <= Mi <= 500.

Формат вывода
В первой строке выведите количество языков, которые знают все школьники. Начиная со
второй строки - список таких языков. Затем - количество языков, которые знает хотя
бы один школьник, на следующих строках - список таких языков.

Пример
Ввод
3
3
Russian
English
Japanese
2
Russian
English
1
English

Вывод
1
English
3
Russian
Japanese
English
"""


def input_data():
    langs: list[set] = []
    n = int(input())
    for i in range(n):
        k = int(input())
        langs.append(set())
        for _ in range(k):
            langs[i].add(input())
    return langs


def work(langs: list[set]):
    know_langs = set(langs[0])
    all_langs = set(langs[0])
    for i in range(1, len(langs)):
        know_langs &= langs[i]
        all_langs |= langs[i]

    return know_langs, all_langs


if __name__ == "__main__":
    # список с языками, каждого школьника
    langs = input_data()
    # получаем множества языков, которые
    # одновременно знают все школьники
    # и языки которые знает хотябы один школьник
    know_langs, all_langs = work(langs)

    # вывод языков которые знают все школьники
    print(len(know_langs))
    for lang in know_langs:
        print(lang)
    # Языки которые знает хотябы один школьник
    print(len(all_langs))
    for lang in all_langs:
        print(lang)
