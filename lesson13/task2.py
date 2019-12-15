f = open('payments.txt')
lst = []
 
for line in f:
    if 'out' in line:
        name, summ,*others = line.strip().split(';') 
        lst.append(name)
        lst.append(summ)
print(max(lst)) 
