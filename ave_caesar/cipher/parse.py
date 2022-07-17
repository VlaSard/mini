__all__ = ['get_parse']


def get_parse(text_input: str) -> list[str]:
    """Преобразует строку текста в список. Знаки пунктуации, числа отделяет от текста."""

    marks = '!"#$%&()*+,-./:;<=>?@[]^_`{|}~' + "\'"
    text_output = list()
    text_temp = ''

    for i in range(len(text_input)):

        if text_input[i].isspace() or text_input[i] in marks:

            if text_temp:
                text_output.append(text_temp)
                text_temp = ''

            text_output.append(text_input[i])

        elif text_input[i].isalnum():

            if not text_temp:
                text_temp += text_input[i]

            else:

                if text_input[i].isalpha() == text_temp.isalpha():
                    text_temp += text_input[i]

                else:
                    text_output.append(text_temp)
                    text_temp = ''
                    text_temp += text_input[i]

    text_output.append(text_temp)

    return text_output
