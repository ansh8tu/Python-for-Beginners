import random

try:
    startRange = int(input('Enter the starting range : '))
    endingRange = int(input('Enter the ending range : '))
    randomNumber = random.randint(startRange, endingRange)
    print(f'Your lucky number for the day is : {randomNumber}')

except ValueError:
    print('Enter input in form of integer and not words!')