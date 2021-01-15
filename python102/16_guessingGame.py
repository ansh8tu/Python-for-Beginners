secretNumber = 7
noOfGuesses =0
guessLimit = 3

while noOfGuesses < guessLimit:
    enteredNumber = int(input('Guess any number(0-9) : '))
    noOfGuesses+=1
    #condition checking
    if enteredNumber == secretNumber:
        print('You\'ve got the secret number!')
        #using break to exit loop once done
        break
else:
    print('Sorry, you\'ve exceeded the number of attempts' )   
