#Using " " for short strings
introduction = "Hello, My name is Ansh"
print(introduction)
print(type(introduction))

#Using ''' ''' for long strings 
longIntro = ''' 
Hello, My name is Anshman, I am trying to give you a brief about me,
I like to Listen songs and play pc Games 
Sounds boring, but duh!
 '''
print(longIntro)

#to print the first character of the string 
print(introduction[0])

#to print first three characters
print(introduction[:4])

#to print the last charater 
print(introduction[-1])

#to copy string
copy = introduction[:]
print(copy)