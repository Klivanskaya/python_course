import math
num = int(input("number is: "))
power = int(input("power is: "))
answer = math.pow(num, power)
another = num ** power
print("number in degree math.pow is: " , answer)
print(type(answer))
print("number in degree ** is: " , another)
print(type(another))
