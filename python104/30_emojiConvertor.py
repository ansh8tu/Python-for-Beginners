print('Hey, How are you feeling today!')
moodToday = input('>').upper().split()
output =">"

emojiConvertor = {
    'HAPPY' : '😊',
    'SAD' : '😔'
}

for word in moodToday: 
    output += emojiConvertor.get(word, word) + " "

print(output)

