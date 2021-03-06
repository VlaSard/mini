def user_survey(messages: str, default: bool = True) -> bool:
    """Опрос пользователя.

     В переменной messages передается часть сообщения. Остальная часть сообщения формируется в функции,
     на основе значения из default, и представляет собой варианты выбора ответа на вопрос.
     В необязательной переменной default передается вариант ответа по умолчанию и равен True.
     При ответе который не поддерживается функцией, выводится сообщение с вариантами ответов,
     и переход к ожиданию ответа пользователя.

     В зависимости от ответа пользователя функция возвращает булево значение равное True или False.
     Ответ может быть введен в любом регистре, полный или сокращенный вариант, на английском или русском языках.

    Args:
        messages (str): строка текста с вопросом,
        default (bool, необязательный): ответ по умолчанию, равен True.

    Returns:
        bool: ответ пользователя.
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

        # Проверяем flag и возвращаем True или  False.
        if len(flag) == 0:
            return default

        if flag in yes:
            return True

        if flag in no:
            return False

        # Если ответ не поддерживается.
        print(f"Требуется ввести {yes_or_no}. Повторите попытку.")
