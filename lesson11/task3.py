import random

lst = dir(__builtins__)[80:] 
lst.remove('copyright')
lst.remove('credits') 
funcs = [getattr(__builtins__, attr) for attr in lst]
while True:
    answer = (input(random.choice(lst)))
    if answer == 'stop':
            break
            
