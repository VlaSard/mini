def day_in_month(current_month: int, current_year: int) -> tuple[int, bool]:
    """The function determines how many days are in a month, given the year type.
    Works for prime year and leap year.

    The input data, month number and year number, must be of type int and have positive values.

    The output is the number of days in a month and the type of year.

    If the year is a leap year it will return True, for a non-leap year it will return False.

    Args:
        current_month (int): month number.
        current_year (int): month number.

    Returns:
        tuple[int, bool]: the number of days in a month and the type of year.
    """

    # Arguments validation.
    if isinstance(current_month, bool) or (isinstance(current_year, bool)):
        raise TypeError("Unsupported data type. Arguments must be of type int.")

    if (isinstance(current_month, int) or isinstance(current_year, int)) is False:
        raise TypeError("Unsupported data type. Arguments must be of type int.")

    if (current_month or current_year) <= 0:
        raise ValueError("The value cannot be negative.")

    # Determining the type of the year.
    # 1 is a leap year, 0 is a non-leap year.
    leap_year = (1 - (current_year % 4 + 2) % (current_year % 4 + 1)) * (current_year % 100 + 2) % (
        current_year % 100 + 1) + (1 - (current_year % 400 + 2) % (current_year % 400 + 1))

    # Calculation of the number of days in a month, taking into account the type of year.
    days_month = 28 + (current_month + (current_month // 8)) % 2 + 2 % current_month + (
        1 + leap_year) // current_month + (1 // current_month) - leap_year // current_month

    return days_month, bool(leap_year)
