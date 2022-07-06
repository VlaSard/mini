# Консольная игра "Угадай слово"
#

from random import randint
from re import findall
from linecache import getline


def random_word(filename: str) -> list:
    """Читаем случайную строку из файла словаря.

    Args:
        filename (str): Имя файла словаря.

    Returns:
        list: Случайное слово из словаря.
    """

    say = list()

    # Открываем файл на чтение.
    with open(filename, 'r') as file:

        # Подсчитывает количество непустых строк в файле.
        lines = len(findall(r".+\n*", file.read()))

        # Генерируем номер случайной строки, не больше числа строк.
        line = num_rnd(lines)

        # Читаем строку с номером line
        say.extend([getline(filename, line)[:-1]][0])

    return say


def num_rnd(end: int) -> int:
    """Генератор случайного числа от 1 до значения end.

    Args:
        end (int): Конечное значение для генератора.

    Returns:
        int: Случайное число.
    """

    return randint(1, end)


def is_answer(messages: str, default: bool = True) -> bool:
    """Опрос пользователя.

     Выводим сообщение с вопросом, получаем ответ пользователя.
     Возвращать True или False.

    Args:
        messages (str): Сообщение с вопросом.
        default (bool, необязательный): Ожидаемый ответ. По умолчанию True.

    Returns:
        bool: Ответ пользователя.
    """

    # Варианты ответов для "ДА"
    yes = ['д', 'да', 'y', 'yes']

    # Варианты ответов для "НЕТ"
    no = ['н', 'нет', 'n', 'no']

    # Формируем строку с вариантами ответов. Буден выведена в сообщении.
    yes_or_no = f'(д/н или да/нет: ' + ('да' if default else 'нет') + ' - по умолчанию): '

    # Ожидание ответа пользователя.
    while True:

        # flag с ответом пользователя.
        flag = input(f'{messages} {yes_or_no}').strip().lower()

        # Проверяем flag и возвращаем True или False.
        if len(flag) == 0:
            return default

        if flag in yes:
            return True

        if flag in no:
            return False

        # Если ответ не поддерживается.
        print(f"Требуется ввести {yes_or_no}. Повторите попытку.")


def mesh(words: list, n: int) -> list:
    """Создаем рабочую сетку.

    Длина сетки равна длине слова, плюс пять ячеек.
    В первых ячейках находятся открытые буквы слова, по одной букве в ячейке.
    Остальные, не открытые буквы заменены символом '-' (минус).
    Ячейка с индексом [-2] используется для счетчика оставшихся попыток.

    Args:
        words (list): Загаданное слово.
        n (int): Счетчик попыток.

    Returns:
        list: Рабочая сетка.
    """

    """     Строим рабочую сетку.     """
    mesh_solve = list()

    # Создаем сетку по длине загаданного слова, заполненную символами "-".
    for _ in range(len(words)):
        mesh_solve.append('-')

    # Дополняем еще 5, незаполненных, ячеек для вывода счетчика ходов.
    for k in range(5):
        mesh_solve.append(' ')

    # Заполняем поля сетки служебной информацией.
    mesh_solve[-3] = 'Осталось'
    mesh_solve[-2] = n
    mesh_solve[-1] = 'попыток'

    """     Открываем буквы в случайных ячейках.     """
    # Определяем сколько букв открыть.
    for _ in range(2 if len(words) > 10 else 1):

        # Определяем номер случайной ячейки.
        i = num_rnd(len(words) - 1)

        # Если букв несколько отрываем все.
        if words.count(words[i]) == 1:
            mesh_solve[i] = words[i]
            continue
        else:
            j = 0
            for _ in range(words.count(words[i])):
                j = words.index(words[i], j)
                mesh_solve[j] = words[j]
                j += 1

    return mesh_solve


def games(amt: int, flag: bool) -> bool:
    """Логика игры.

    Args:
        amt (int): Счетчик оставшихся попыток.
        flag (bool): Начать или окончить игру.

    Returns:
        bool: True или False, отгадано слово или нет.
    """

    while flag:

        # Если счетчик ходов больше 0.
        if amt > 0:

            # Ожидание ввода буквы.
            while True:

                char = input(f'Введите букву которая, по вашему мнению, есть в этом слове - ').upper()

                if char not in [chr(code) for code in range(ord('А'), ord('Я') + 1)]:
                    print(f'Необходимо ввести букву русского алфавита (регистр не имеет значения).\n')
                    continue
                else:
                    break

            cou = word.count(char)

            idx = 0

            # Проверка наличия буквы в слове.
            if char in word:

                # Открываем все буквы если их несколько.
                for _ in range(cou):
                    idx = word.index(char, idx)
                    mesh_to_solve[idx] = word[idx]
                    idx += 1
            else:

                amt -= 1

                # Прописывает количество оставшихся ходов.
                mesh_to_solve[-2] = amt

                if amt == 1:
                    mesh_to_solve[-3] = 'Осталась'
                    mesh_to_solve[-1] = 'попытка'
                elif 1 < amt < 5:
                    mesh_to_solve[-1] = 'попытки'
                elif amt > 4:
                    mesh_to_solve[-1] = 'попыток'

            # Выводим игровую сетку с изменениями.
            print('\n', *mesh_to_solve, '\n')

            # Проверка слова. Отгадано или нет.
            if mesh_to_solve[:len(word)] != word:
                continue
            # Если слово отгадали, выходим.
            break

        # Если счетчик ходов < 0, выходим со значением False.
        flag = False

    return flag


# Выводим приветствие.
print(f'Добро пожаловать в игру "Угадай слово".'
      f'\nДается 6 попыток отгадать загаданное слово. Попытки списываются только за'
      f'\nнеправильный вариант. Первоначально может быть открыто от одной и более букв.'
      f'\nЖелаем удачи.\n\n')

# Устанавливаем флаг game в True или False.
game = is_answer('Начнем?')

while game:

    # Задаем число попыток.
    attempts = 6

    # Загадываем слово.
    word = random_word("dict.ru")

    # Создаем игровую сетку и выводим ее.
    mesh_to_solve = mesh(word, attempts)
    print('\n', *mesh_to_solve, '\n')

    # Запускаем игру.
    if games(attempts, game):
        print(f'Поздравляем! Вы смогли отгадать слово.\n')
    else:
        print(f'К сожалению вы не смогли отгадать слово.\n')
    game = is_answer('Хотите сыграть еще?', False)
