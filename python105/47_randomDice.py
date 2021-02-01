import random

'''
numberOfRolls = int(input('Enter the number of times you want to roll the dice : '))

for number in range(numberOfRolls):  
    firstNumber = random.randint(1,6)
    secondNumber = random.randint(1,6)
    print(f'({firstNumber}, {secondNumber})')
'''

class Dice:
    def roll():
         firstNumber = random.randint(1,6)
         secondNumber = random.randint(1,6)
         return firstNumber, secondNumber

try :
    numberOfRolls = int(input('Enter the number of times you want to roll the dice : '))

    for number in range(numberOfRolls):  
        print(Dice.roll())

except ValueError:
    print('Enter an integer type value')