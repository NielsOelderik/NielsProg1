def convert(Celsius):
    Fahrenheit = ((Celsius * 1.8) + 32)
    return(Fahrenheit)
def table():
    for x in range(-30, 40, 10):
        print('{0:6} {1:6}'.format(convert(x), x))

print('{0:2} {1:5} {2:5}'.format('','F:','C:'))
table()