num = int(input('Enter you number:'))
form = input('укажите, в каком представлении вывести число - бинарном B, 8-миричном O, 16-ричном H: ').upper()
if form == 'В':
    print(bin(num))
elif form == 'O':
    print(oct(num))
elif form == 'H':      
    print(hex(num))
else:     
    print('Error')
print('До свидания!')
