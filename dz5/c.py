"""
C. Туризм

Александр недавно увлекся горным туризмом. Ему уже надоело покорять отдельные
горные пики, и он собирается покорить самую настоящую горную цепь!
Напомним, что Александр живет в плоском мире. Горная цепь состоит из отрезков,
соединяющих точки на плоскости, каждая из которых находится строго правее
предыдущей (x-координата следующей точки больше, чем у предыдущей). Трассой на
горной цепи называется её часть между двумя фиксированными концами отрезков.

Участок, на котором при движении по трассе координата y (высота) всегда
возрастает, называется подъемом, величиной подъема называется разность
высот между начальной и конечной точками участка.

Туристическая компания предлагает на выбор несколько трасс на одной горной цепи.
Александр из-за финансовых трудностей может выбрать для поездки только одну из
этих трасс. Вы решили помочь ему с выбором. Александру важно для каждой трассы
определить суммарную высоту подъемов на ней. Обратите внимание, что трасса может
идти как слева-направо, так и справа-налево.

Формат ввода
В первой строке входного файла содержится единственное число N — количество
точек ломаной, задающей горную цепь (1 <= N <= 30000). Далее в N строках
содержатся описания точек, каждое из которых состоит из двух целых чисел,
xi и yi (1 <= xi, yi <= 30000).
В следующей строке находится число M — количество трасс (1 <= M <= 30000).

Далее в M строках содержатся описания трасс. Каждое описание представляет
собой два целых числа, si и fi, они обозначают номера вершин начала и конца
трассы, соответственно (1 <= si <= N, 1 <= fi <= N). Начало и конец трассы
могут совпадать.
Гарантируется, что во входном файле задана именно горная цепь.

Формат вывода
Для каждой трассы выведите одно число —
суммарную высоту подъемов на данной трассе.

Пример 1
7
2 1
4 5
7 4
8 2
9 6
11 3
15 3
1
2 6
Вывод
4

Пример 2
Вывод
6
1 1
3 2
5 6
7 2
10 4
11 1
3
5 6
1 4
4 2
Вывод
0
5
4
"""


def input_data():
    n = int(input())
    y = []
    for _ in range(n):
        xi, yi = map(int, input().split())
        y.append(yi)

    m = int(input())
    routes = []
    for _ in range(m):
        si, fi = map(int, input().split())
        routes.append((si-1, fi-1))

    return n, y, m, routes


def solve(n, y, m, routes):
    # префиксный массив прямого прохода
    pref_go = [0] * n
    for i in range(1, n):
        if y[i] > y[i-1]:
            pref_go[i] += y[i] - y[i-1]
        pref_go[i] += pref_go[i-1]

    # префиксный массив обратного прохода
    pref_back = [0] * n
    for i in range(n-2, -1, -1):
        if y[i] > y[i+1]:
            pref_back[i] += y[i] - y[i+1]
        pref_back[i] += pref_back[i+1]

    res = []
    for s, f in routes:
        if s < f:
            res.append(pref_go[f] - pref_go[s])
        else:
            res.append(pref_back[f] - pref_back[s])
    return res


if __name__ == "__main__":
    n, y, m, routes = input_data()
    res = solve(n, y, m, routes)
    print(*res, sep="\n")
