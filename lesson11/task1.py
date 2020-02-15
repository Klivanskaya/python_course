import string
import random

l = []
code = list(string.ascii_lowercase)
nl = random.sample(code, 10)
s = input('Enter your string: ')
for i in s:
    l.extend(nl)
    l.append(i)
    
my_string = ''.join(l) 
print(my_string)   
