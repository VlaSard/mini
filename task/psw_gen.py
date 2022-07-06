"""
Генератор паролей с настройкой и возможностью записи списка паролей в файл.
"""
import random
from string import ascii_lowercase, ascii_uppercase, digits

# Первоначальное значение, для запуска программы.
answer = True


def get_pools(message, default):
    """
    Функция обработки ответа пользователя на запросы программы.
    Возвращаемое значение по умолчанию передается в переменной default.
    В переменной message передаем сообщение с вопросом.

    При не допустимом ответе на запрос: выводится сообщение с допустимыми вариантами ответа.
    Возвращаем True или False.

    :param message: сообщение, которое будет выведено в запросе.
    :type message: str
    :param default: возвращаемое значение по умолчанию True или False.
    :type default: bool
    :return: ответ пользователя.
    :rtype: bool
    """
    yes = ['д', 'да', 'y', 'yes']
    no = ['н', 'нет', 'n', 'no']
    yes_or_no = f'(д/н или да/нет: ' + ('да' if default else 'нет') + ' - по умолчанию): '
    while True:
        flag = input(f'{message} {yes_or_no}').strip().lower()
        if len(flag) == 0:
            return default
        if flag in yes:
            return True
        if flag in no:
            return False
        print(f"Требуется ввести {yes_or_no}. Повторите попытку.")


def get_password(len_pas, chars):
    """
    Функция генератора пароля заданной длинны.
    На вход передаем список символов и длину пароля.

    :param len_pas: длинна пароля.
    :type chars: list
    :param chars: символы для пароля.
    :type len_pas: int
    :return: строка содержащая пароль.
    :rtype: str
    """
    return ''.join([random.choice(chars) for _ in range(len_pas)])


def get_password_list(number):
    """
    Функция создает список паролей.
    На входе указываем количество паролей. На выходе получаем список.

    :type number: int
    :param number: количество паролей.
    :return: список паролей.
    :rtype: list[str]
    """
    psw_list = list()
    for i in range(number):
        psw_list.append(get_password(length, char_list))
    return psw_list


def get_chars():
    """
    Функция настройки списка символов.
    Задает какие символы будут использоваться в пароле.

    :return: список символов.
    :rtype: list
    """
    punctuation = '!#$%&*+-=?@^_'
    chars = list()
    if get_pools(f'В пароле использовать цифры?', True):
        chars.extend(digits)
    if get_pools(f'В пароле использовать буквенные символы нижнего регистра?', True):
        chars.extend(ascii_lowercase)
    if get_pools(f'В пароле использовать буквенные символы верхнего регистра?', True):
        chars.extend(ascii_uppercase)
    if get_pools(f'В пароле использовать знаки пунктуации?', False):
        chars.extend(punctuation)
    random.shuffle(chars)
    if get_pools(f'Исключать неоднозначные символы il1LoO0?', False):
        for char in 'il1LoO0':
            chars.remove(char)
    return chars


def get_answer(messages):
    """
    Функция запроса длинны и количества паролей.

    :param messages: сообщение.
    :type messages: str
    :return: возвращаем числовое значение.
    :rtype: int
    """
    while True:
        answer_in = input(f'{messages}: ')
        if not answer_in.isdigit():
            print(f'Допустимое значение - числовое. Попробуйте еще раз.')
        else:
            return int(answer_in)


def get_output_pas(password):
    """
    Функция записывает в файл или выводит в консоль список паролей.

    :param password: список паролей
    :type password: list[str]
    :return:
    """
    if get_pools(f'Сохранить пароли в файл?', True):
        file_pass = open('password.txt', 'w')
        file_pass.write('\n'.join(password))
        file_pass.close()
    else:
        print(f'Список паролей:')
        for psw in pass_list:
            print(psw)


while answer:
    length = get_answer(f'Введите длину генерируемого пароля')
    amount = get_answer(f'Введите количество необходимых паролей')

    # Создаем список символов для генерации пароля.
    char_list = get_chars()

    # Создаем список паролей.
    pass_list = get_password_list(amount)

    # Записываем в файл или выводим в консоль список паролей.
    get_output_pas(pass_list)

    # Запрос на создание еще одного списка.
    answer = get_pools(f'Продолжить?', False)
