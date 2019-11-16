import string
st = tuple(dir(string))
print('Тупл с 5 последними атрибутами модуля string: ' , st[-5:])
result = list(st[-5:])
index = 2
result.insert (index , 'capwords')
print('Тупл с добавленной строкой capwords: ' , tuple(result))
