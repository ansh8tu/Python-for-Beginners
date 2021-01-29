from largestNumModule import *

num = int(input('Enter the number of elements you want to insert in your list : '))
numberList = []

for number in range(num):
    numberEntered = int(input(f'Enter element at index {number} : '))
    numberList.append(numberEntered)

print(f'The list of numbers entered by you are : {numberList}')

finalOutput = findLargestNum(numberList)
print(f'The largest number in list is : {finalOutput}')


