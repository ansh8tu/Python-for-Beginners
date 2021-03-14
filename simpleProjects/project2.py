from tkinter import *

root = Tk()
root.title("Anshuman's Calculator")
root.iconbitmap('allImagesUsed/calc.ico')

userInput = Entry(root, width=40, borderwidth=4)
userInput.grid(row='0', column='0', columnspan='4', padx='10',pady='10')


def whenPressed(number):
    currentNumber = userInput.get()
    userInput.delete(0, END)
    value = str(currentNumber) + str(number)
    userInput.insert(0,value)

def whenClearPressed():
    userInput.delete(0, END)

def whenAddPressed():
    firstNumber = userInput.get()
    global fNum
    global userOperator
    userOperator = 'add'
    fNum = int(firstNumber)
    userInput.delete(0, END)

def whenMultiplyPressed():
    firstNumber = userInput.get()
    global fNum
    global userOperator
    userOperator = 'multiply'
    fNum = int(firstNumber)
    userInput.delete(0, END)
    
    
def whenDividePressed():
    firstNumber = userInput.get()
    global fNum
    global userOperator
    userOperator = 'divide'
    fNum = int(firstNumber)
    userInput.delete(0, END)
    

def whenSubPressed():
    firstNumber = userInput.get()
    global fNum
    global userOperator
    userOperator = 'sub'
    fNum = int(firstNumber)
    userInput.delete(0, END)
    

def whenEqualPressed():
    secondNumber = userInput.get()
    userInput.delete(0, END)

    if userOperator == 'add':
        userInput.insert(0, fNum + int(secondNumber))
    
    if userOperator == 'sub':
        userInput.insert(0, fNum - int(secondNumber))
    
    if userOperator == 'multiply':
        userInput.insert(0, fNum * int(secondNumber))

    if userOperator == 'divide':
            userInput.insert(0, fNum / int(secondNumber))
        
  
    
#creating buttons
button0 = Button(root, text= '0', padx=40, pady=20, command=lambda : whenPressed(0), bg='black', fg='white')

button1 = Button(root, text= '1', padx=40, pady=20, command=lambda :whenPressed(1), bg='black', fg='white')
button2 = Button(root, text= '2', padx=40, pady=20, command=lambda :whenPressed(2), bg='black', fg='white')
button3 = Button(root, text= '3', padx=40, pady=20, command=lambda :whenPressed(3), bg='black', fg='white')

button4 = Button(root, text= '4', padx=40, pady=20, command=lambda :whenPressed(4), bg='black', fg='white')
button5 = Button(root, text= '5', padx=40, pady=20, command=lambda :whenPressed(5), bg='black', fg='white')
button6 = Button(root, text= '6', padx=40, pady=20, command=lambda :whenPressed(6), bg='black', fg='white')

button7 = Button(root, text= '7', padx=40, pady=20, command=lambda :whenPressed(7), bg='black', fg='white')
button8 = Button(root, text= '8', padx=40, pady=20, command=lambda :whenPressed(8), bg='black', fg='white')
button9 = Button(root, text= '9', padx=40, pady=20, command=lambda :whenPressed(9), bg='black', fg='white')

buttonAdd = Button(root, text= '+', padx=40, pady=20, command=whenAddPressed,bg='green', fg='white')
buttonSub = Button(root, text= '- ', padx=40, pady=20, command=whenSubPressed,bg='maroon', fg='white')
buttonMultiply = Button(root, text= 'x', padx=41, pady=20, command=whenMultiplyPressed, bg='orange', fg='white')
buttonDivide = Button(root, text= '/ ', padx=40, pady=20, command=whenDividePressed, bg='blue', fg='white')

buttonEqual = Button(root, text= '=', padx=40, pady=20, command=whenEqualPressed)
buttonClear = Button(root, text='Clear ', padx=28, pady=20, command=whenClearPressed, bg='#ff4242', fg='white' )

#displaying buttons
button0.grid(row='4', column='0')

button1.grid(row='3', column='0')
button2.grid(row='3', column='1')
button3.grid(row='3', column='2')

button4.grid(row='2', column='0')
button5.grid(row='2', column='1')
button6.grid(row='2', column='2')

button7.grid(row='1', column='0')
button8.grid(row='1', column='1')
button9.grid(row='1', column='2')

buttonAdd.grid(row='1', column='3')
buttonSub.grid(row='2', column='3')
buttonMultiply.grid(row='3', column='3')
buttonEqual.grid(row='4', column='1')
buttonClear.grid(row='4', column='2')
buttonDivide.grid(row='4',column='3')

root.mainloop()
