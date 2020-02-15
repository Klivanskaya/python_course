f = open('weather.txt')
lst = []
temp_list = []
my_d = {}
for line in f:
    date, temp = line.strip().split(';')
    lst.append((date, int(temp)))
    temp_list.append(int(temp))
    my_d[int(temp)] = date
print(min(temp_list), max(temp_list))
print(sum(temp_list)/len(temp_list))
print(len(my_d))
