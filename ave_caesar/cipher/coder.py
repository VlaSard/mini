__all__ = ['get_coder']

import cipher


def get_coder(word: str, bias: int) -> str:
    """Перекодирует слово по ключу, смещая символы на заданное значение."""

    let_en = [chr(code) for code in range(ord('a'), ord('z') + 1)]
    let_ru = [chr(code) for code in range(ord('а'), ord('я') + 1)]
    line = ''

    for char in word:

        if char.isalpha():

            if cipher.get_language(char) == 'en':

                if char.lower() == char:
                    line += let_en[(let_en.index(char) + bias) % len(let_en)]

                else:
                    line += let_en[(let_en.index(char.lower()) + bias) % len(let_en)].upper()

            if cipher.get_language(char) == 'ru':

                if char.lower() == char:
                    line += let_ru[(let_ru.index(char) + bias) % len(let_ru)]

                else:
                    line += let_ru[(let_ru.index(char.lower()) + bias) % len(let_ru)].upper()

        else:
            line += char

    return line
