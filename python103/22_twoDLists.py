songs = [['Easy Love','Adrenaline', 'Come back home'], ['Sims', 'Believed', 'Sweatpants']]

#prints first list's element at index 1
print(songs[0][1])
songs[1][1] ='Modern Loneliness'
print(songs[1][1])
print()

#prints each song line by line
for album in songs:
    for song in album:
        print(song)
            