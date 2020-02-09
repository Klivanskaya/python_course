import random

class ValueTooBig(ValueError):
    '''input number is too big'''


class ValueTooSmall(ValueError):
    '''input number is too small'''

    
num = int(random.randint(1,100))
print(num)
my_num = input('Enter number: ')

while num != int(my_num):
    try:
        if int(my_num) < num:
            raise ValueTooSmall('введенное число меньше искомого')
        elif  int(my_num) > num:
            raise ValueTooBig('введенное число больше искомого')
        
    except (ValueTooBig, ValueTooSmall) as ex:
        print(ex)
        my_num = input('Enter number: ')
else:
    print('Congrats')
