import string
import random

first = list(string.ascii_lowercase)

n = random.randint(1,28)

second = string.ascii_lowercase[n:]
third = string.ascii_lowercase[:n]
another = list(second + third)

my_dict = dict(zip(first, another))
print(my_dict)
