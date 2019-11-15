import random

number = random.randint(100,999),random.randint(100,999), random.randint(100,999)
sorted_number = sorted(number)
print('Список случайных трехзначных чисел: ' , list(number))
print('Отсортированный в прямом порядке: ' , sorted_number)
print('Отсортированный в обратном порядке: ' , sorted_number[::-1])
