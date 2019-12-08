with open('applog.txt', 'r') as f:
    my_d = {}
    for line in f:
        st = line.split(' ')
        ip = st[0]
        time = st[2]
        d = dict({ip:[time]})
        if ip in my_d:
            old_time = my_d[ip]
            d = dict({ip:([time] + old_time)})
        my_d.update(d)
    print(my_d)
    
