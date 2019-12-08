import string

st = input('Enter your string: ')
lenst = len(st)

while lenst < 2:
    s = input('Enter your string: ')
    print(s)
    lenst = len(s)

second = string.ascii_lowercase[4:]
third = string.ascii_lowercase[:4]
another = list(second + third)
my_dict = dict(zip(s, another))
print(my_dict) 
