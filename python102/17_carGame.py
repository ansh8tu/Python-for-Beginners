userChoice = ''

gameInstructions = '''
Type Start to start the game!
Type Stop to stop the game!
Type Quit to quit the game!

'''
carStarted = False
carStopped = False

while True:
    userChoice = input(' > ').upper()
    if userChoice == 'START':
        if carStarted:
            print('Car already started!')
        else:
            print('Good, hold on tight, the game has begun! ')
            carStarted =True
    elif userChoice == 'STOP':
        if carStopped:
            print('Car already Stopped!')
        else:
            print('Duh, What happened? ')
            carStopped = True
    elif userChoice == 'HELP':
        print(gameInstructions)
    elif userChoice == 'QUIT':
        break
    else:
         print('Sorry, I didn\'t get what you wanted to say!')
    
        

    
    