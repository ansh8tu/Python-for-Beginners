class MusicPlayer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f'The name of song  is : {x}')
        print(f'The name of artist is : {y}')
    


songName = input('> Enter the name of song : ')
artistName = input('> Enter the name of artist : ')

print('Constructor Calling! ')
song = MusicPlayer(songName,artistName)

