print("Welcome to Tip Calculator\n")

totalBill = float(input("What was the total bill?\n$"))
tipPercent = int(input("What percentage tip would you like to give?\n"))
numOfPeople = int(input("How many people to split the bill?\n"))

tipPer = (1 + (tipPercent/100))
billAmount = round(((totalBill * tipPer)/numOfPeople), 2)

#in od=rder to format upto two decimal places
billAmount = '{:.2f}'.format(billAmount);

print(f'Each person should pay ${billAmount}')