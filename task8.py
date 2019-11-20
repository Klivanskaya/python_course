name = input("Enter your name and surname: " ).split()
age = str(input("Enter your age:  "))
position = str(input("Enter your position:  "))
salary = str(input("Enter your salary:  "))

print(f"name is: <{name[0]}>," , f"surname is: <{name[1]}>")
print(f"age is: <{age}>")
print(f"position is: <{position}>")
print(f"salary is: <{salary}>")

#второй способ форматирования
name = (input("Enter your name and surname: " )).split()
age = input("Enter your age:  ")
position = input("Enter your position:  ")
salary = input("Enter your salary:  ")

print("name is: <{}>,".format(name[0]) , "surname is: <{}>".format(name[1]))
print("age is: <{}>".format(age))
print("position is: <{}>".format(position))
print("salary is: <{}>".format(salary))
