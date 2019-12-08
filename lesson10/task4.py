import random

num = int(random.randint(1,100))
print(num)
my_num = input('Enter number: ')
while num != int(my_num):
    if int(my_num) < num:
        print('введенное число меньше искомого')
        my_num = input('Enter number: ')
    elif  int(my_num) > num:
        print('введенное число больше искомого')
        my_num = input('Enter number: ')
else:
    print('Congrats')  
