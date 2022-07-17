__all__ = ['get_language']

from re import search


def get_language(char: str) -> str:
    """Возвращает принадлежность символа к языку. Возвращает 'en' или 'ru'"""

    flag = ''

    if bool(search('[a-z]', char[0].lower())):
        flag = 'en'

    if bool(search('[а-я]', char[0].lower())):
        flag = 'ru'

    return flag
