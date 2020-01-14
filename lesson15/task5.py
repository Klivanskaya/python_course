import string

my_dict = {}
txt = input("Enter your text: ").lower()

for letter in txt:
    if letter in string.ascii_lowercase:
        if letter in my_dict:
            my_dict[letter]+=1
        else: 
            my_dict[letter]=1     

print(my_dict)  
