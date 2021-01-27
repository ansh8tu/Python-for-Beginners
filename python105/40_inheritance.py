class Artist:
    def isSingingSong(songName):
        print(f'Playing {songName} right away!')


class LauvSongs(Artist):
    def pauseSong(songName):
        print('Paused!')


class JeremyZucker(Artist):
    pass

songName = input('>Enter the name of the song that you want to play : ')
LauvSongs.isSingingSong(songName)
LauvSongs.pauseSong(songName)
