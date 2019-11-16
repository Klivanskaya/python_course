import string
st = tuple(dir(string))
print(len(st))
print('Тупл с 5 последними атрибутами модуля string: ' , st[20:25])
result = list(st[20:25])
index = 2
result.insert (index , 'capwords')
print('Тупл с добавленной строкой capwords: ' , tuple(result))
