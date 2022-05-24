"""
Консольная игра "Угадай число".
Написана на Python 3.
"""
from random import randint


# Проверка введённого пользователем числа.
def is_valid(num):
    if num.isdigit():
        if 0 < int(num) < 101:
            return True
    return False


# Проверка введённого пользователем числа и загаданного числа.
def is_check(num_us, num_rnd):
    if num_us == num_rnd:
        print(f'Вы угадали, поздравляем!')
        flag = True
    elif num_us < num_rnd:
        print(f'Ваше число меньше загаданного, попробуйте еще разок')
        flag = False
    else:
        print(f'Ваше число больше загаданного, попробуйте еще разок')
        flag = False
    return flag


# Проверка ответа пользователя на предложение продолжить.
def is_answer(default):
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


# Вывод сообщения о затраченных попытках на отгадывание числа.
def is_counter(counter):
    if counter % 100 // 10 == 1 or counter % 10 in (0, 5, 6, 7, 8, 9):
        ending = 'ов'
    elif counter % 10 in (2, 3, 4):
        ending = 'а'
    else:
        ending = ''
    print(f'\nНа отгадывание числа вы использовали {counter} ход{ending}.')
    return


def main(answer):
    number_rand = randint(1, 10)
    counter = 0
    while answer:
        user_number = input(f'\nВведите свой вариант числа: ')
        counter += 1
        if is_valid(user_number):
            user_number = int(user_number)
            if is_check(user_number, number_rand):
                is_counter(counter)
                if is_answer(False):
                    main(True)
                else:
                    print(f'\nСпасибо, что играли в "Угадай число". Еще увидимся...')
                answer = False
        else:
            print(f'А может быть все-таки введем целое число от 1 до 100?')
    return 0


if __name__ == '__main__':
    print(f'\nДобро пожаловать в игру "Угадай число".\n')
    main(True)
