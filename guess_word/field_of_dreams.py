from random import randint
from re import findall
from linecache import getline


filename = 'resources/dict_ru'
expression = list()

with open(filename, 'r') as file:
    lines = len(findall(r".+\n*", file.read()))
    expression.extend(getline(filename, randint(1, lines))[:-1].split(': '))

print(expression)
