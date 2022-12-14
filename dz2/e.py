"""
E. Чемпионат по метанию коровьих лепешек

Ежегодный турнир «Веселый коровяк» — по метанию коровьих лепешек на
дальность — прошел 8–9 июля в селе Крылово Осинского района Пермского края.

Участники соревнований кидают «снаряд» — спрессованный навоз, выбирая его из
заранее заготовленной кучи. Желающих поупражняться в силе броска традиционно
очень много — как мужчин, так и женщин. Каждую лепешку, которую метнули
участники «Веселого коровяка», внимательно осматривали женщины в костюмах коров
и тщательно замеряли расстояние.

Соревнования по метанию коровьих лепешек проводятся в Пермском крае с 2009 года.
К сожалению, после чемпионата потерялись записи с фамилиями участников, остались
только записи о длине броска в том порядке, в котором их совершали участники.

Трактиорист Василий помнит три факта:
    1) Число метров, на которое он метнул лепешку, оканчивалось на 5
    2) Один из победителей чемпионата метал лепешку до Василия
    3) Участник, метавший лепешку сразу после Василия, метнул ее на меньшее количество метров

Будем считать, что участник соревнования занял k-е место, если ровно (k - 1) участников
чемпионата метнули лепешку строго дальше, чем он.
Какое максимально высокое место мог занять Василий?

Формат ввода
Первая строка входного файла содержит целое число n — количество участников
чемпионата по метанию лепешек (3 <= n <= 10^5).
Вторая строка входного файла содержит n положительных целых чисел, каждое
из которых не превышает 1000, — дальность броска участников чемпионата,
приведенные в том порядке, в котором происходило метание.

Формат вывода
Выведите самое высокое место, которое мог занять тракторист Василий. Если
не существует ни одного участника чемпионата, который удовлетворяет,
описанным выше условиям, выведите число 0.

Пример 1
Ввод                Вывод
7                   6
10 20 15 10 30 5 1

Пример 2
Ввод	   Вывод
3          1
15 15 10

Пример 3
Ввод	    Вывод
3           0
10 15 20

комментарий: победители - те, кто занял первое место (их может быть несколько)
Хотя по логике надо учитывать еще и 2-3 места.
"""


def input_data():
    n = int(input())
    nums = [int(x) for x in input().split()]
    return nums


def work(nums: list):
    # счёт победителя
    win_score = nums[0]
    # флаг, что нашли такого Василия
    isHave = False
    for i in range(1, len(nums) - 1):
        # счёт i-го игрока
        x = nums[i]
        # если счёт текущего игрока больше счёта победителя
        if x > win_score:
            # изменяем счёт победителя
            win_score = x
            # опускаем флаг, что нашли Василия
            isHave = False
        # Если текущий игрок со счёт меньшим или равным победителю
        # проверяем соответствуюет ли он 1 и 3 условию Василия
        elif (x % 10 == 5) and x > nums[i + 1]:
            # Если соответсвует, то проверям находилили такого Василия до этого
            # Если не находили
            if not isHave:
                # Нужно задать счёт Василия
                vas_score = x
                # И поднять флаг, что нашли его
                isHave = True
            # Иначе если такого Васю уже находили
            # Проверяем, вдруг у текущего игрока счёт больше чем у Васи
            # И в то же время он соответсвует Всем условиям
            elif x > vas_score:
                # Тогда нужо просто обновить счёт Василия
                vas_score = x

    # Если не нашли такого Василия
    if not isHave:
        return 0

    # Если мы здесь, то мы нашли такого Василия
    # Получаем его место вторым проходом
    k = 0
    for x in nums:
        if x > vas_score:
            k += 1
    return k + 1


if __name__ == "__main__":
    nums = input_data()
    res = work(nums)
    print(res)
