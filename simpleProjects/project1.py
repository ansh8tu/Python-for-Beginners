from functools import reduce

userName = input('Enter your name : ')

projectDescription = f'''
Hello {userName}, This is a project to calculate the sum and product of first 'n' 
natural numbers, this project asks your input for the value of n, let's say
you give the value of n=4, then it returns the value as follows:

The sum of first 4 natural numbers is : 10
The product of first 4 natural numbers is : 24

Have a nice day, :))

'''

print(projectDescription)

userInput = int(input('Enter the value of n : '))
print()
userList = []

for number in range(1, userInput + 1):
    userList.append(number)

multiply = reduce(lambda x,y: x*y, userList)
add = reduce(lambda x,y: x+y, userList)

print(f'The sum of first {userInput} natural numbers is : {add}')
print(f'The product of first {userInput} natural numbers is : {multiply}')
print()
