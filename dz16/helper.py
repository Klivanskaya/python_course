
# - функция get_random_list(n, a, b) для генерации списка из n случайных чисел в 
# заданном диапазоне (a, b); 
import random


def get_random_list(n, a, b):
    '''this is get_random_list'''
    res = []
    while len(res)!= n:
        r = random.randint(a, b)
        res.append(r)
    return res


# - функция get_random_password(n) генерации пароля - 
# формирует пароль из n символов - буквы, большие, маленькие, цифры; 
import string


def get_random_password(n):
    '''this is get_random_password'''
    symbols = string.ascii_letters + string.digits
    result = random.sample(symbols, n)
    return ''.join(result)


# функция подсчет слов в тексте get_words_count(text)


def get_words_count(text):
    '''this is get_words_count'''
    f = open(text)
    my_list = []
    for i in f:
        a = i.strip().split()
        a.sort(key=len)
    return len(a)


# функция получения списка слов (без знаков препинания и тп) get_words(file_name) из файла


def get_words(file_name):
    '''this is get_words'''
    lst = []
    f = open(file_name)
    for i in f:
        lst = i.strip().split(' ')
        return lst


if __name__ == "__main__":
    print(get_random_list, get_random_list.__doc__)
    print(get_random_password, get_random_password.__doc__)
    print(get_words_count, get_words_count.__doc__)
    print(get_words, get_words.__doc__)

