try:
    age = int(input('> Enter your age in number : '))
    print(f'You are : {age} years old!')

except ValueError:
    print('Invalid Input!')

except ZeroDivisionError:
    print('Age can\'t be zero')