def parse_line(line):
    # f = open('weather.txt')
    date, temp = line.strip().split(';')
    return date, int(temp)

  
def parse_file():
    f = open('weather.txt')
    weather = {}
    for line in f:
        d, t = parse_line(line)
        weather[t] = d
    return weather

def find_min_or_max(stat, func):
    temp = func(stat)
    # max_temp = max(stat)
    return temp

weather = parse_file()
print(find_min_or_max(weather, min))
print(find_min_or_max(weather, max))
