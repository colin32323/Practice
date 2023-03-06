import random


def check(num, guess, last):
    if num == guess:
        print("Correct guess\n")
        return True
    elif guess < num:
        if guess in range(num-int(last*0.15), num):
            print('Low but close\n')
        else:
            print("Too low\n")
        return False
    else:
        if guess in range(num+1, num+int(last*0.15)):
            print('High but close\n')
        else:
            print('Too high\n')
        return False


end = 1000
running = True
number = random.randint(1, end)
count = 1
while running:
    choice = int(input('Enter your guess : '))
    if check(number, choice, end):
        running = False
