def day_in_month(current_month: int, current_year: int) -> tuple[int, bool]:
    """Функция определяет, сколько дней в месяце.
    Работает для простого и високосного года.

    Входные данные: номер месяца и номер года.
    На выходе получаем количество дней в месяце и признак високосного года.
    Если год високосный вернет True, для невисокосного года - False.

    Args:
        current_month (int): номер месяца,
        current_year (int): номер года.

    Returns:
        tuple[int, bool]: количество дней в месяце и признак високосного года.
    """

    # Проверка аргументов
    if (isinstance(current_month, int) or isinstance(current_year, int)) is False:
        raise TypeError("Не поддерживаемый тип данных.")

    if (current_month or current_year) <= 0:
        raise ValueError("Значение не может быть отрицательным.")

    # Признак високосного года: 1 - год високосный, 0 - невисокосный.
    leap_year = (1 - (current_year % 4 + 2) % (current_year % 4 + 1)) * (current_year % 100 + 2) % (
        current_year % 100 + 1) + (1 - (current_year % 400 + 2) % (current_year % 400 + 1))

    # Количество дней в месяце.
    days_month = 28 + (current_month + (current_month // 8)) % 2 + 2 % current_month + (
        1 + leap_year) // current_month + (1 // current_month) - leap_year // current_month

    return days_month, bool(leap_year)
