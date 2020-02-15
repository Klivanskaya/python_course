payments = {}

with open('payments.txt', 'r') as f:

    for line in f:
        
        # 1. распарсить 
        splitted = line.split(';')
        if len(splitted) < 5:
            continue
        name, amount, date, ptype,*others = splitted

        # 2. анализировать
        if ptype != 'out':
            continue
        amount = float(amount.split()[0].replace(',', '.'))
        
        # 3. поместить в структуру данных
        if name in payments:
            payments[name].append(amount)
        else:
            payments[name] = [amount]

        max_count_person = ''
        max_count = 0
        name_one = ''
        sum_one = 0
        for name, sums in payments.items():
            if len(sums) > max_count:
                max_count = len(sums)
                max_count_person = name
            if sum(sums) > sum_one:
                sum_one = len(sums)
                name_one = name    

print(max_count_person, max_count)
