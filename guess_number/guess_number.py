# Консольная игра "Угадай число".
# 
# Компьютер загадывает случайное число из диапазона введенного человеком.
# Задача игрока за наименьшее число ходов определить загаданное число.
# Для разных операций в программе используются функции

from random import randint


def is_input_range() -> tuple[int, int]:
    """Запрос начального и конечного значений диапазона.

    Возвращает два числовых значения. Начало диапазона и конец диапазона.

    Returns:
        tuple[int, int]: Начальное и конечное значение диапазона.
    """
    while True:
        try:
            number_min, number_max = input(f'Введите диапазон, в котором будет загадано случайное число (например '
                                           f'1-100): ').split("-")
        except ValueError:
            print(f'Введите границы диапазона через тире. Например 1-100.')
        else:
            if number_min.isdigit() and number_max.isdigit():
                return int(number_min), int(number_max)
            print(f'Должно быть указано целое числовое значение.')


def is_number_rand(start_number: int, stop_number: int) -> int:
    """Генератор случайных чисел с заданным диапазоном.

    Возвращает случайное число из диапазона start_number <= x <= stop_number.

    Args:
        start_number (int): Начало диапазона.
        stop_number (int): Конец диапазона.

    Returns:
        int: Случайное число.
    """
    return randint(start_number, stop_number)


def is_user_number(number_min: int, number_max: int) -> int:
    """Ввод пользователем числа.

    Проверяет корректность ввода. 
    Возвращает числовое значение.

    Args:
        number_min (int): Начало диапазона.
        number_max (int): Конец диапазона.

    Returns:
        int: Значение введенное пользователем.
    """
    while True:
        num = input(f'\nВведите свой вариант числа: ')
        if num.isdigit() and number_min <= int(num) <= number_max:
            return int(num)
        else:
            print(f'А может быть все-таки введем целое число от {number_min} до {number_max}?')


def is_check(number_usr: int, number_rnd: int) -> bool:
    """Проверка равенства числа введенного пользователем и загаданного.

    По результатам проверки выводим соответствующие сообщения. 
    Возвращаем True если значения равны, и False если не равны.

    Args:
        number_usr (int): Число введенное пользователем.
        number_rnd (int): Случайное загаданное число.

    Returns:
        bool: Возвращаем истина или ложь.
    """
    if number_usr == number_rnd:
        print(f'Вы угадали, поздравляем!')
        flag = True
    elif number_usr < number_rnd:
        print(f'Ваше число меньше загаданного, попробуйте еще разок')
        flag = False
    else:
        print(f'Ваше число больше загаданного, попробуйте еще разок')
        flag = False
    return flag


def is_counter(counter: int):
    """Отображение сообщения о потраченных попытках угадать число.

    Args:
        counter (int): Количество попыток.
    """
    if counter % 100 // 10 == 1 or counter % 10 in (0, 5, 6, 7, 8, 9):
        ending = 'ов'
    elif counter % 10 in (2, 3, 4):
        ending = 'а'
    else:
        ending = ''
    print(f'\nНа отгадывание числа вы использовали {counter} ход{ending}.')
    return


def is_answer(default: bool) -> bool:
    """Проверка ответа пользователя на предложение продолжить.

    Args:
        default (bool): Ответ по умолчанию.

    Returns:
        bool: Возвращаем истина или ложь.
    """
    yes = ['д', 'да', 'y', 'yes']
    no = ['н', 'нет', 'n', 'no']
    yes_or_no = f'(д/н или да/нет: ' + ('да' if default else 'нет') + ' - по умолчанию): '
    while True:
        flag = input(f'\nХотите попробовать еще раз? {yes_or_no}').strip().lower()
        if len(flag) == 0:
            return default
        if flag in yes:
            return True
        if flag in no:
            return False
        print(f"Требуется ввести {yes_or_no}. Повторите попытку.")


def main(answer: bool, number_rand: int, num_min: int, num_max: int, counter: int = 0):
    """Логика игры.

    Args:
        answer (bool): Значение для запуска игры. При старте равно True.
        number_rand (int): Загаданное число.
        num_min (int): Начало диапазона.
        num_max (int): Конец диапазона.
        counter (int, необязательный): Счетчик ходов. По умолчанию 0.
    """
    # Игровой цикл, пока answer = true.
    while answer:

        # Ввод пользователем числа.
        user_number = is_user_number(num_min, num_max)
        
        # Увеличиваем счетчик попыток на 1.
        counter += 1

        # Пользователь отгадал число?
        if is_check(user_number, number_rand):

            # Если отгадал, выводим сколько попыток было использовано.
            is_counter(counter)

            # Будем играть еще?
            if is_answer(False):

                # Если да - запускаем еще раз.

                # Выбор диапазона, в котором будет загадано число.
                num_min, num_max = is_input_range()

                # Загадываем число.
                number_rand = is_number_rand(num_min, num_max)

                # Запускаем логику игры.
                main(True, number_rand, num_min, num_max)

            else:
                # Если нет - выводим сообщение и завершаем программу.
                print(f'\nСпасибо, что играли в "Угадай число". Еще увидимся...')
            answer = False

    return


if __name__ == '__main__':
    # Если не импортируем, то запускаем.

    # Выводим приглашение.
    print(f'\nДобро пожаловать в игру "Угадай число".\n')

    # Выбор диапазона, в котором будет загадано число.
    min_number, max_number = is_input_range()

    # Загадываем число.
    num_rand = is_number_rand(min_number, max_number)

    # Запускаем логику игры.
    main(True, num_rand, min_number, max_number)
