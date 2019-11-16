import string
string = input('Enter your string: ')
string = list(sorted(string))
my_string = " ".join(string)
print("Елементы строки в прямом порядке: " , my_string)
print("Елементы строки в обратном порядке: " , my_string[::-1])
