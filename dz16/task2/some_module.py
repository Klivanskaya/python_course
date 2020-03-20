import string
import random


# шифрация
def encode(text):
    second = string.ascii_lowercase[3:]
    third = string.ascii_lowercase[:3]
    another = list(second + third)
    my_dict = dict(zip(text, another))
    return my_dict


# print(encode('Nastya'))


# дешифрация
def decode(text):
    first = list(string.ascii_lowercase)
    s = list(text)
    my_dict = dict(zip(first,s))
    return my_dict


# print(decode('Nastya'))