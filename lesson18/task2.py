name = input('Enter your name: ')
l = name.split(' ')
if len(l) != 2:
    raise Exception('Enter name and surname')


year = input('Enter your birth year: ')
if not year.isdigit():
    raise Exception('format your year')

if int(year) > 1999:
    raise Exception('format your year')

month = input('Enter your birth month: ')
if not month.isdigit():
    raise Exception('format your month')
if int(month) > 12:
    raise Exception('format your year')

date = input('Enter your birth day: ')
if not date.isdigit():
    raise Exception('format your year')
if month in (1,3,5,7,8,10,12):
    if int(date) > 31:
        raise Exception('max days is 31')
elif month == 2:
    if int(date) > 28:
        raise Exception('max days is 28')
else:
    if int(date) > 30:
        raise Exception('max days is 30')

profession = input('Enter your profession: ')

bith_date = f'{date}.{month}.{year}'

with open(f'{name}.txt', 'w') as f:
    f.write(f'name is: {name}''; 'f'bith date is: {bith_date}''; 'f'profession is: {profession}''\n')
    f.close()
    
    
