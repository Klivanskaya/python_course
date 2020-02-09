with open('parslog.log', 'r') as f:

    for line in f:
        try:
            if '[ERROR]' in line:                
                splitted = line.split(';')
                ls = []
                for i in splitted:
                    ls.append(i)
                           
                with open('errors.log', 'a') as f:
                    f.writelines(ls)
                    f.close()
        except Exception:
            raise Exception('line format is not true')    
        
