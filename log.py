import math


def log(value):
    return math.log(value, 2)


while True:
    num = int(input('-> '))
    if num == 0:
        break
    print(log(num), end='\n\n')
