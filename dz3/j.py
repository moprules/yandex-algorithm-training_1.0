"""
Дороги Нью-Манхэттена устроены следующим образом. С юга на север через каждые сто метров проходит авеню, с запада на восток через каждые сто метров проходит улица. Авеню и улицы нумеруются целыми числами. Меньшие номера соответствуют западным авеню и южным улицам. Таким образом, можно построить прямоугольную систему координат так, чтобы точка (x, y) лежала на пересечении x-ой авеню и y-ой улицы. Легко заметить, что для того, чтобы в Нью-Манхэттене дойти от точки (x1, y1) до точки (x2, y2) нужно пройти |x2 − x1| + |y2 − y1| кварталов. Эта величина называется манхэттенским расстоянием между точками (x1, y1) и (x2, y2).

Миша живет в Нью-Манхэттене и каждое утро делает пробежку по городу. Он выбегает из своего дома, который находится в точке (0, 0) и бежит по случайному маршруту. Каждую минуту Миша либо остается на том же перекрестке, что и минуту назад, или перемещается на один квартал в любом направлении. Чтобы не заблудиться Миша берет с собой навигатор, который каждые t минут говорит Мише, в какой точке он находится. К сожалению, навигатор показывает не точное положение Миши, он может показать любую из точек, манхэттенское расстояние от которых до Миши не превышает d.

Через t × n минут от начала пробежки, получив n-е сообщение от навигатора, Миша решил, что пора бежать домой. Для этого он хочет понять, в каких точках он может находиться. Помогите Мише сделать это.

Формат ввода
Первая строка входного файла содержит числа t, d и n (1 ≤ t ≤ 100, 1 ≤ d ≤ 100, 1 ≤ n ≤ 100).

Далее n строк описывают данные, полученные от навигатора. Строка номер i содержит числа xi и yi — данные, полученные от навигатора через ti минут от начала пробежки.

Формат вывода
В первой строке выходного файла выведите число m — число точек, в которых может находиться Миша. Далее выведите m пар чисел — координаты точек. Точки можно вывести в произвольном порядке.

Гарантируется, что навигатор исправен и что существует по крайней мере одна точка, в которой может находиться Миша.

Пример 1
Ввод
2 1 5
0 1
-2 1
-2 3
0 3
2 5
Вывод
2
1 5
2 4

Пример 2
Ввод
1 1 1
0 0
Вывод
5
-1 0
0 -1
0 0
0 1
1 0

Пример 3
Ввод
1 10 1
0 0
Вывод
5
-1 0
0 -1
0 0
0 1
1 0
"""


class Field:
    """Класс области в повёрнутой системе координат"""

    def __init__(self, cx=0, cy=0, p=0, q=0) -> None:
        cur_p = cx - cy
        self.p1 = cur_p - p
        self.p2 = cur_p + p
        cur_q = cx + cy
        self.q1 = cur_q - q
        self.q2 = cur_q + q

    def __str__(self):
        p1 = self.p1
        p2 = self.p2
        q1 = self.q1
        q2 = self.q2
        return f"p={p1}, {p2}; q={q1}, {q2}"

    def __repr__(self):
        return str(self)

    def __and__(self, other):
        """Перегрузка оператора & - пересечение"""
        # Результирующее поле
        res_field = Field()
        # левый край
        res_field.p1 = max(self.p1, other.p1)
        res_field.q1 = max(self.q1, other.q1)
        # Правый край
        res_field.p2 = min(self.p2, other.p2)
        res_field.q2 = min(self.q2, other.q2)
        return res_field

    def __iand__(self, other):
        """Перегрузка оператора &= - пересечение c присовением"""
        # левый край
        self.p1 = max(self.p1, other.p1)
        self.q1 = max(self.q1, other.q1)
        # Правый край
        self.p2 = min(self.p2, other.p2)
        self.q2 = min(self.q2, other.q2)
        return self

    def expand(self, t: int):
        """Расширить область на t во все стороны"""
        self.p1 -= t
        self.q1 -= t
        # Правый край
        self.p2 += t
        self.q2 += t

    def show(self):
        # Собираем результирующий массив точек
        res_mas = []
        for p in range(self.p1, self.p2 + 1):
            for q in range(self.q1, self.q2 + 1):
                if (p + q) % 2 == 0:
                    x = (q + p) // 2
                    y = (q - p) // 2
                    res_mas.append((x, y))

        # Выводи количество точек
        print(len(res_mas))
        # выводим сами точки
        for (x, y) in res_mas:
            print(x, y, sep=" ")


def input_data():
    t, d, n = map(int, input().split())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    return t, d, n, points


def work(t, d, n, points):
    # Создаём стартовое поле,
    res_field = Field(0, 0)
    for (x, y) in points:
        # Увеличиваем размеры результирующего поля на t
        # - это та область, в которой человек может находиться
        # в текущий момент времени
        res_field.expand(t)
        # Получаем поле текущей точки с навигатора
        cur_field = Field(x, y, d, d)
        # пересекаем полученные поля, обновляя результирующее поле
        res_field &= cur_field

    # Выводим результирующее множество
    res_field.show()


if __name__ == "__main__":
    t, d, n, points = input_data()
    work(t, d, n, points)
