with open('weather.txt', 'r')  as f:
    one = f.readlines()
    lst = ''.join(one).split('\n')
    my_d = {}
    for i in lst:
        a = i.split(';')
        my_d.update({a[0]:a[1]})
    minimum = 0
    maximum = 0
    for k, v in my_d.items():
        temp = 0
        days = 0
        if int(v) < int(minimum):
            minimum = v
            t = f'{k}:{minimum}'
        elif int(v) > int(maximum):
            maximum = v
            m = f'{k}:{maximum}'
        temp += int(v)
        days += 1
    print(t)
    print(m)
    print(int(temp/days))
