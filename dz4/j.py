"""
J. Дополнительная проверка на списывание

Преподаватель курса ОиМП заказал у одного известного психолога полное
психологическое обследование всех студентов, поступивших на ФНК с целью выяснить
их склонность к списыванию еще до начала занятий и отчислить их за списывание еще
до того как они приступят к занятиям и смогут позорить ФНК своими преступлениями.
Психолог, привлеченный для проведения обследования, известен своим инновационным
методом, позволяющим понять склонность к списыванию студента по наиболее часто
используемому им в программах идентификатору. Помогите известному психологу определить,
какие из студентов потенциально являются преступниками. Напишите программу,
которая по приведенной программе выяснит наиболее часто используемый в ней
идентификатор.

Поскольку разные студенты на тестировании пишут программы на разных языках
программирования, ваша программа должна уметь работать с произвольным языком.
Поскольку в разных языках используются различные ключевые слова, то список
ключевых слов в анализируемом языке предоставляется на вход программе.
Все последовательности из латинских букв, цифр и знаков подчеркивания,
которые не являются ключевыми словами и содержат хотя бы один символ,
не являющийся цифрой, могут быть идентификаторами. При этом в некоторых языках
идентификаторы могут начинаться с цифры, а в некоторых - нет. Если идентификатор
не может начинаться с цифры, то последовательность, начинающаяся с цифры,
идентификатором не является. Кроме этого, задано, является ли язык чувствительным
к регистру символов, используемых в идентификаторах и ключевых словах.

Формат ввода
В первой строке вводятся число n - количество ключевых слов в языке (0 <= n <= 50)
и два слова C и D, каждое из которых равно либо "yes", либо "no".
Слово C равно "yes", если идентификаторы и ключевые слова в языке чувствительны
к регистру символов, и "no", если нет. Слово D равно "yes", если идентификаторы
в языке могут начинаться с цифры, и "no", если нет.

Следующие n строк содержат по одному слову, состоящему из букв латинского алфавита
и символов подчеркивания - ключевые слова. Все ключевые слова непусты, различны,
при этом, если язык не чувствителен к регистру, то различны и без учета регистра.
Длина каждого ключевого слова не превышает 50 символов.

Далее до конца входных данных идет текст программы. Он содержит только символы
с ASCII-кодами от 32 до 126 и переводы строки.

Размер входных данных не превышает 10 килобайт. В программе есть хотя бы один идентификатор.

Формат вывода
Выведите идентификатор, встречающийся в программе максимальное число раз. Если таких
идентификаторов несколько, следует вывести тот, который встречается в первый раз раньше.
Если язык во входных данных не чувствителен к регистру, то можно выводить идентификатор
в любом регистре.

Пример 1
Ввод
0 yes no
int main() {
  int a;
  int b;
  scanf("%d%d", &a, &b);
  printf("%d", a + b);
}

Вывод
int


Пример 2
Ввод
0 yes no
#define INT int
int main() {
  INT a, b;
  scanf("%d%d", &a, &b);
  printf("%d %d", a + b, 0);
}

Вывод
d


Пример 3
Ввод
6 no no
program
var
begin
end
while
for
program sum;
var
  A, B: integer;
begin
  read(A, b);
  writeln(a + b);
end.

Вывод
a


Пример 4
Ввод
1 yes yes
_
a = 0h
b = 0h
c = 0h

Вывод
0h
"""

from collections import defaultdict
import sys


def get_indets(line: str, isDig: bool):
    res = []
    indet = ""
    # проходимся по всем символам в стркое
    for c in line:
        if c.isalpha() or c.isdigit() or c == "_":
            indet += c
        else:
            if indet and (not indet.isdigit()) and ((not indet[0].isdigit()) or isDig):
                res.append(indet)
            indet = ""

    if indet:
        res.append(indet)

    return res


def solve():
    # n - количество слов в словаре
    # isReg - язык регистрозависимый
    # isDig - идентификатор может начинаться с цифры
    n, isReg, isDig = input().strip().split()
    # Переводим флаги в более простую форму True - False
    isReg = isReg == "yes"
    isDig = isDig == "yes"

    # Собираем множество ключевых слов языка
    keywords = set()
    for _ in range(int(n)):
        word = input().strip()
        if not isReg:
            word = word.lower()
        keywords.add(word)
    # словарь счётчик идентификаторов
    counts = defaultdict(lambda: {"pos": 0, "cnt": 0})
    # счётчик уникальных идентификаторов
    unics_cnt = 0
    # Идентификатор, встречающийся в коде максмиальое количество раз
    myMax = None
    # пробегаемся по всем стркоам кода
    for line in sys.stdin:
        # Пробегаемся по всем найденным идентификаторам в строке
        for indet in get_indets(line.strip(), isDig):
            # Если код регистроНЕзависимый
            if not isReg:
                # Приводим все идентификотры к одному стилю
                # В нижнем регистре
                indet = indet.lower()
            # Если текущего идентификатора нет в ключевых словах
            if indet not in keywords:
                # Если идентификатор нам УЖЕ встречался
                if indet not in counts:
                    # Увеличиваем счётчик уникальных идентификаторов
                    unics_cnt += 1
                    # Задаём позицию новому идентификатору
                    counts[indet]["pos"] = unics_cnt
                # увеличиваем счётчик этого идентификатора в коде
                counts[indet]["cnt"] += 1
                # Обновляем идентификатор с максимальным упоминанием в коде,
                # если потребуется
                if counts[myMax]["cnt"] < counts[indet]["cnt"] or (
                    counts[myMax]["cnt"] == counts[indet]["cnt"]
                    and counts[myMax]["pos"] > counts[indet]["pos"]
                ):
                    myMax = indet

    return myMax


if __name__ == "__main__":
    res = solve()
    print(res)
