def get_result(func, *args):

    if func in (len, sum, min, max):
        for i in args:
            a = func(i)
            print(a)
    else:
        print('Not valid func') 
        
        
get_result(len, 'jgfhfs', 'khfgj', 'khacj')

