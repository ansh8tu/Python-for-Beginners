#program to remove duplicates from a list
numbers =[10, 20, 5, 10, 2, 3]
newList=[]

for number in numbers:
    if number not in newList:
        newList.append(number)

print(newList)