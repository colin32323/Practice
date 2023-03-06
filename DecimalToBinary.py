def decimal_to_binary(value):
    binary = ''
    temp = value
    while temp > 0:
        binary = str(temp % 2) + binary
        temp = temp // 2
    return int(binary)


while True:
    num = int(input('(0 to exit)\n-> '))
    if num == 0:
        break
    print(decimal_to_binary(num), end='\n\n')
