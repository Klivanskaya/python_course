import random

first_num = random.uniform(1,100)
second_num = random.uniform(1,100)
print("First number is: " , first_num)
print("Second number is: " , second_num)
result = first_num * second_num
print('number rounded to four digits is: ' , round(result, 4))
print('number rounded to two digits is: ' , round(result, 2))
