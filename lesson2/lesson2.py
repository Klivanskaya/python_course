import math
import random

innum = random.randint(1,100)
flonum = random.uniform(1,100)
print(innum, flonum)
print("Is innum bigger than flonum number?", innum > flonum )


a = random.randint(1,100)
b = random.randint(1,100)
print(a)
print(b)
a > b
print(a > b)

num = int(input("number is: "))
power = int(input("power is: "))
answer = math.pow(num, power)
another = num ** power
print("Answer is ", answer)
print(type(answer))
print(another)
print(type(another))

n = random.randint(1,100)
print(n)
square = math.pow(n, 2)
print(square)
print(n > 10)
print(square > 500)

first = int(input('Enter your number: '))
print(hex(first))
print(oct(first))