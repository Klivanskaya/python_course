with open('persons.txt', 'r') as f:
    one, two = f.readlines()
    print(one, two)
   
a = one.split(';')
b = two.split(';')
c = ''.join(a).split()
d = ''.join(b).split()

harry_dict = {
            'name': {'first_name': c[0], 'last_name': c[1]},
            'age': int(c[2]),
            'profession': c[5],
            'salary':{'amount': float(c[3]), 'currency': c[4]}
            }
ross_dict = {
            'name': {'first_name': d[0], 'last_name': d[1]},
            'age': int(d[2]),
            'profession': d[5],
            'salary':{'amount': float(d[3]), 'currency': d[4]}
            }

result = {'ross': ross_dict, 'harry': harry_dict}
print(result)
