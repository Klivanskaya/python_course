import string
st = tuple(dir(string)[-5:])
print('Тупл с 5 последними атрибутами модуля string: ' , st)
result = list(st[-5:])
result.insert (2, 'capwords')
print('Тупл с добавленной строкой capwords: ' , tuple(result))
