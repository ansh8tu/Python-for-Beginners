
class Song:
    def playSong(songName):
        print(f'Playing {songName} right away!')
    
    def pauseSong(songName):
        print(f'Pause {songName}')


songName = input('> Enter the name of the song you want to play : ')

songToPlay = Song()
Song.playSong(songName)
Song.pauseSong(songName)
