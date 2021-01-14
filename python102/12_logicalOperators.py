##user gives input in the form of string 
input1 = input('Enter first number : ')
input2 = input('Enter second number : ')

print(type(input1)) 
print(type(input2))

input1AsInt = int(input1)
input2AsInt = int(input2)

sum = input1AsInt + input2AsInt
print(sum)

if sum == 7 and input1AsInt <7:
    print('Sum is equal to 7 and your first number is less than 7')
elif sum>7 or input2AsInt > 7:
    print('Sum is greater than 7 or second number is greater than 7')
else:
    print('Sum is less than 7')

#and, or, not are logical operators


