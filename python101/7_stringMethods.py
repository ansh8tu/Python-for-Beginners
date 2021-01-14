playlist = "My playlist has 100+ songs"
print(len(playlist))

#printing the playlist in uppercase 
#A point to notice is that .upper() is a method and not a function
print(playlist.upper())

#printing in lower case
print(playlist.lower())

#for finding any character we use find 
#returns the index with first occurence of p
print(playlist.find('p'))

#to replace something
#replaces 100 with 200
print(playlist.replace('100', '200'))

#to check if a string exists or not
#returns true
print('playlist' in playlist)