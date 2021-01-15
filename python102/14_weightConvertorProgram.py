weight = input('Enter you weight : ')
lbsOrKg = input("Specify units i.e. 'l/L' for lbs(pounds) or 'k/K' for Kg : ")

#it could also be written as lbsOrKg.upper() == 'L' 
if lbsOrKg == 'l' or lbsOrKg =='L':
    weightInKg = 0.453592 * float(weight) 
    print(f'Weight in kg : {weightInKg}')
    
elif lbsOrKg == 'k' or lbsOrKg == 'K':
    weightInPounds = 2.20462 * float(weight) 
    print(f'Weight in kg : {weightInPounds}')
    
else:
    print('Entry valid entry for units!')
