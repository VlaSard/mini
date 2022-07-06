# Шифр Цезаря (шифр сдвига) — один из самых простых и наиболее широко известных методов шифрования.
# Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом,
# находящимся на некотором постоянном числе позиций левее или правее него в алфавите.
#
# На вход программе подается строка текста, которую нужно зашифровать.
# Зашифровать можно всю строку с одним сдвигом или зашифровать каждое слово со сдвигом равном длине слова.
# Строчные буквы при этом остаются строчными, а прописные – прописными. Знаки пунктуации не меняются.
#
# Для кодирования передаем смещение.
# Для декодирования смещение = плотность алфавита - исходное смещение.
# Для ru index=32-n, для en index=26-n.

from re import search


def get_coder(line_old, offset):
    """
    Перекодируем слово по ключу.

    На вход подается слово, ключ кодирования.

    Язык слова определяется автоматически по первому символу.

    Если в одном слове, без пробелов, встречаются символы из разных языков вызовет ошибку.

    :type line_old: str
    :type offset: int
    :rtype: str
    """
    line_new = ''
    letters = ''
    # Определяем язык строки.
    if bool(search('[a-z]', line_old[0].lower())):
        letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
    elif bool(search('[а-я]', line_old[0].lower())):
        letters = [chr(code) for code in range(ord('а'), ord('я') + 1)]
    # Кодируем строку.
    for char in line_old:
        if char.lower() == char:
            line_new += letters[(letters.index(char) + offset) % len(letters)]
        else:
            line_new += letters[(letters.index(char.lower()) + offset) % len(letters)].upper()
    return line_new


def get_parse_string(text_old):
    """
    Разбираем строку текста.

    На вход подается строка текста. На выходе получаем список.
    Буквенные символы, цифры и знаки пунктуации записываются отдельно.

    'Пример строки на входе: 5р67.'

    ['Пример', ' ', 'строки', ' ', 'на', ' ', 'выходе', ':', '5', 'р', '67', '.']

    :type text_old: str
    :rtype: list[str]
    """
    punctuation = '!"#$%&()*+,-./:;<=>?@[]^_`{|}~' + "\'"
    text_new = list()
    text = ''
    for index in range(len(text_old)):
        if text_old[index].isspace() or text_old[index] in punctuation:
            if text:
                text_new.append(text)
                text = ''
            text_new.append(text_old[index])
        elif text_old[index].isalnum():
            if not text:
                text += text_old[index]
            else:
                if text_old[index].isalpha() == text.isalpha():
                    text += text_old[index]
                else:
                    text_new.append(text)
                    text = ''
                    text += text_old[index]
    text_new.append(text)
    return text_new


def get_concatenate_string(string_list):
    """
    Получаем строку текста из списка.

    На вход подается список. На выходе получаем строку текста.


    ['Пример', ' ', 'списка', ' ', 'на', ' ', 'входе', '.']

    'Пример строки на выходе.'

    Аналог ''.join(s). Ну а вдруг.

    :type string_list: str
    :rtype: str
    """
    line = ''
    for word in string_list:
        line += word
    return line


def get_decode_list(str_decode, bias):
    """
    Из полученного списка читаем элементы и если это строка отправляем на кодировку.

    На вход подается строка подлежащая кодированию и ключ кодирования,
    для выбора кодирования по длине слова, вместо ключа передаем False.

    :param str_decode: строка текста.
    :type str_decode: list[str]
    :param bias: смещение.
    :type bias: int
    :return: перекодированная строка.
    :rtype: list[str]
    """
    str_line = list()
    for i in range(len(str_decode)):
        # Определяем ключ кодирования
        bias = len(str_decode[i]) * mode * route if bias is False else bias
        # Если элемент списка текст, передаем на кодировку.
        if str_decode[i].isalpha():
            str_line.append(get_coder(str_decode[i], bias))
        else:
            str_line.append(str_decode[i])
    return str_line


def get_polls(msg, default, key_1, key_2):
    """
    Вывод запросов о режимах.

    :type msg: str
    :type default: bool
    :type key_1: str
    :type key_2: str
    :rtype: bool
    """
    while True:
        reply = input(f'{msg} {key_1}/{key_2} ({key_1} - по умолчанию): ')
        if reply == key_1 or len(reply) == 0:
            return default
        if reply == key_2:
            return False
        print(f'Необходимо ввести {key_1} или {key_2}.')


print(f'Добро пожаловать в программу Caesar.')

answer = True

while answer:

    # Режим работы: шифровать / дешифровать.
    mode = 1 if get_polls(f'Выберите режим: шифровать / дешифровать текст', True, 'ш', 'д') else -1

    # Направление кодировки.
    route = 1 if get_polls(f'Выберите направление кодировки (вправо / влево)', True, 'п', 'л') else -1

    # Текст для обработки.
    text_in = get_parse_string(input(f'Введите текст для кодировки:\n'))

    # Ключ кодирования.
    while True:
        key = input(f'Введите ключ (по умолчанию ключ равен длине слова): ')
        if len(key) == 0 or key == '0':
            key = False
            break
        elif key.isdigit():
            key = int(key) * route * mode
            break
        else:
            print(f'Необходимо ввести число или нажать "Enter".')

    # Обработка текста.
    text_ou = get_decode_list(text_in, key)
    print(f'Исходный текст успешно обработан:', ''.join(text_ou), sep='\n')

    # Запрос продолжения работы.
    answer = get_polls(f'Обработать еще один текст?', False, 'н', 'д')
