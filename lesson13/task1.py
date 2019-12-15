import string
import random

l = []
code = list(string.ascii_lowercase)
nl = random.sample(code, 10)
s = input('Enter your string: ')
for i in s:
    l.append(i)
    l.extend(nl)
my_string = ''.join(l) 
print(my_string[::11]) 
