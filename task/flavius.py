# N человек, пронумерованных числами от 1 до N, стоят в кругу. Они начинают считаться,
# каждый K-й по счету человек выбывает из круга, после чего счет продолжается со следующего
# за ним человека. Определяем номер человека, который останется в кругу последним.

"""  Решение с рекурсией  """


def flavius(n, k):
    """

    :param n:
    :type n: int
    :param k:
    :type k: int
    :return:
    :rtype: int
    """
    if n == 1:
        return 1
    elif n > 1:
        x = 1 + (flavius(n - 1, k) + k - 1) % n
        return x


n = 7
k = 5
print(flavius(n, k))

"""  Решение с циклом  """
people = 2
step = 1
survivor = 0
for i in range(1, people + 1):
    survivor = (survivor + step) % i
print(survivor + 1)

"""  Вариант императивного решения  """
people = 2
step = 1
# Список заполняем значениями от 1 до people.
survivor = list(range(1, people + 1))
# Список для выбывших.
block = list()
# Пока в списке не останется один элемент.
while people - 1:
    # Индекс ячейки выбывшего.
    i = (step - 1) % people
    # Добавляем в конец списка выбывших.
    block.append(survivor[i])
    # Список оставшихся переписываем с удалением выбывшего. Хвост списка записываем в начало,
    # в конец добавляем начало списка.
    survivor = survivor[i + 1:] + survivor[:i]
    # Уменьшаем значение оставшихся.
    people -= 1
# В списке по индексу 0 оставшийся, его и выводим.
print(survivor[0])

"""  Вариант решения в лоб.  """
people = 498
step = 68
# Список people заполняем значением True.
survivor = list(True for _ in range(people))
# Индекс проверяемой ячейки.
i = 0
# Пока в списке не останется 1 элемента True.
while people - 1:
    # Сколько ячеек нужно проверить.
    j = step - 1
    # Пока не проверим все ячейки.
    while j > 0:
        # Если в ячейке True - индекс ячейки + 1, шаг - 1.
        if survivor[i]:
            i = (i + 1) % len(survivor)
            j -= 1
        # Если в ячейке False - индекс ячейки + 1, шаг не меняем.
        else:
            i = (i + 1) % len(survivor)
    # Если в ячейке False, ищем ближайшую со значением True.
    while survivor[i] is False:
        i = (i + 1) % len(survivor)
    # Меняем в ячейке True на False, уменьшаем значение people на 1, увеличиваем индекс на 1.
    survivor[i] = False
    people -= 1
    i = (i + 1) % len(survivor)
# Выводим индекс ячейки со значением True + 1, т.к. нумерация индексов начинается с 0.
print(survivor.index(True) + 1)
