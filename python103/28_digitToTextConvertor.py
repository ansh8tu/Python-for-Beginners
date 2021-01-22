phoneNumber = input("Enter your Phone number : ")

digitConvertor = {
    '0': 'Zero',
    '1': 'One',
    '2':'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'    
}

for number in phoneNumber:
    print(digitConvertor.get(number), end = " ")