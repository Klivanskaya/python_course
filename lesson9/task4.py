import random

numbers = random.randint(1, 100)

num = input('enter your number: ')
if num.isalpha() == True:
    print('Число сгенерировано: ' , numbers, 'Квадрат числа: ', int(numbers)*int(numbers))
else:
    print('Число: ', num, 'Квадрат числа: ', int(num)*int(num))
    
