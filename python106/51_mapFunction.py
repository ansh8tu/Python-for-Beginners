#so basically map function expects two arguments one is the function and other is the iterable 
#for example lets print the length of each item in songs list 

songs = ['havana', 'sims', 'sweatpants']

def lengthOfItems(songs):
    return len(songs)

idk = map(lengthOfItems, songs)
print(list(idk))
