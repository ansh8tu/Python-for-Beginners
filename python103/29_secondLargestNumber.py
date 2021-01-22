n = int(input())
arr = list(map(int, input().split()))
maxScore = 0
nonDuplicateNumbers = []

for number in arr:
    if number not in nonDuplicateNumbers:
        nonDuplicateNumbers.append(number)
nonDuplicateNumbers.sort()
nonDuplicateNumbers.reverse()

print(nonDuplicateNumbers[1])
