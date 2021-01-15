username = input('Username : ')
password = input('Password : ')

if len(username) < 3:
    print('Username must have at least 3 characters, Try again!')
elif len(password) < 3:
    print('Password must have at least 3 characters, Try again!') 
else:
    print('Username & Password Successfully set!')