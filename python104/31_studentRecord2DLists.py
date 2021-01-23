numStudents = int(input())
studentData = []
awardList = []

#getting input from the user and storing it in a list 
for student in range(numStudents):
    name = input()
    score = float(input())
    studentData += [[name, score]]
    awardList +=[score]

#to remove the duplicate scores you can use set as well followed by sorted function
nonDuplicateMarks = []
for marks in awardList:
    if marks not in nonDuplicateMarks:
        nonDuplicateMarks.append(marks)

nonDuplicateMarks.sort()
secondLowestMarks = nonDuplicateMarks[1]


for i,j in sorted(studentData):
    if(j == secondLowestMarks):
        print(i)



