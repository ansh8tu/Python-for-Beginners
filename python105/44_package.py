from concert.concertCost import *

noOfPeople = int(input('Enter the number of people : '))
totalCost = cost(noOfPeople)

print(f'The cost of tickets is : ${totalCost}')