#so basically lambda functions are used to you know replace functions like we cannd add two numbers by using two ways
#first is defining a function

def addNumbers(x, y):
    return x + y

print(f'Result : {addNumbers(10,20)} ')

#second way is to use lambda functions

addNumber = lambda x,y:x+y
print(f'Result : {addNumber(10, 20)} ')

#another cool example of lambda functions is to sort a list 

coOrdinates = [(10,20), (1, 4), (8,11), (5, 23)]

sortedCoOrdinates = sorted(coOrdinates, key = lambda x: x[0])
print(sortedCoOrdinates)

#else you would'v written 
def sortNumbers(x):
    return x[0]

sortedWRTX = sorted(coOrdinates, key= sortNumbers)
sortedWRTY = sorted(coOrdinates, key = lambda x : x[1])

print(sortedWRTX)
print(sortedWRTY)