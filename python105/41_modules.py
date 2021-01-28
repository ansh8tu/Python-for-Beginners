import check
from check import *

checkFunction()

name = input('>Enter your name : ').upper()

if name == 'ANSHUMAN':
    check.nameCheck(name)
else:
    print('Access Denied!')