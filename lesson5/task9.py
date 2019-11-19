import random
import string
number = string.digits + string.ascii_letters
lengh = random.randint(10,20)

password = random.sample(number,lengh)
print(password)
