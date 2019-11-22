d = 'ross geller; 34; 6500.45 usd; paleontologist'.split(';')
c = ''.join(d).split()
my_dict = {
            'name': {'first_name': c[0], 'last_name': c[1]},
            'age': int(c[2]),
            'profession': c[5],
            'salary':{'amount': float(c[3]), 'currency': c[4]}
            }
print(my_dict)
