import random

my_list = [random.randint(1,9)] *30
my_list[2::3] = [1000]*10
print(my_list)
print(len(my_list))
