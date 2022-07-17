import cipher


def unpack(line):
    return ", ".join(map(str, line))


print(f'Добро пожаловать в программу Caesar.')

caesar = True

while caesar:

    # Режим работы: шифровать / дешифровать.
    repl = input(f'\nВыберите режим работы шифровать или дешифровать текст: (по умолчанию шифровать) ')

    while True:

        encrypted = ['encrypt', 'e', 'шифровать', 'ш']
        decrypted = ['decrypt', 'd', 'дешифровать', 'д']

        if len(repl) == 0 or repl in encrypted:
            mode = 1
            break

        elif repl in decrypted:
            mode = -1
            break

        else:
            repl = input(f'Необходимо ввести ([{unpack(encrypted)}] или [{unpack(decrypted)}]): ')

    # Направление кодировки.
    repl = input(f'\nВыберите направление кодировки вправо или влево: (по умолчанию вправо) ')

    while True:

        left = ['left', 'l', 'влево', 'л']
        right = ['right', 'r', 'вправо', 'п']

        if len(repl) == 0 or repl in right:
            route = 1
            break

        elif repl in left:
            route = -1
            break

        else:
            repl = input(f'Необходимо ввести ([{unpack(left)}] или [{unpack(right)}]): ')

    # Определение ключа кодирования.
    key = input(f'\nВведите ключ (по умолчанию ключ равен длине слова): ')

    while True:

        if len(key) == 0 or key == '0':
            key = False
            break

        elif key.isdigit():
            key = int(key) * route * mode
            break

        else:
            key = input('Необходимо ввести число или нажать "Enter": ')

    # Получение текст для обработки.
    text_in = cipher.get_parse(input(f'\nВведите текст для кодировки:\n'))

    # Обработка текста.
    text_ou = list()

    for word in text_in:

        if key is False:
            offset = len(word)

        else:
            offset = key

        text_ou.append(cipher.get_coder(word, offset))

    # Обработка текста завершена.
    print(f'\nИсходный текст успешно обработан:', ''.join(text_ou), sep='\n')

    # Запрос продолжения работы.
    repl = input(f'\nОбработать еще один текст?: (нет - по умолчанию) ')

    while True:

        yes = ['yes', 'y', 'да', 'д']
        no = ['no', 'n', 'нет', 'н']

        if len(repl) == 0 or repl in no:
            caesar = False
            break

        elif repl in yes:
            caesar = True
            break

        else:
            repl = input(f'Необходимо ввести ([{unpack(yes)}] или [{unpack(no)}]): ')
