quastion = input('может летать? ')
if quastion == 'y':
  
    feathers = input('есть перья ?')
    if feathers == 'y':
        print('bird')
        
    else:
        mouse = input('мышь? ')
        if mouse == 'y':
            print('bat')
        else:  
            print('insect')
            
if quastion == 'n':
    fish = input('живет в воде? ')
    if fish == 'y':
        print('fish')
    if fish == 'n':
        leg = input('есть ноги? ')
        if leg == 'n':
            print('snake')
        else:
            print('mammal')
