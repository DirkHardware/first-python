class Song:

    def __init__(self, title, artist, duration):
        self._title = title
        self._artist = artist
        self._duration = duration


class Album:

    def __init__(self, name, year, artist=None):
        self._name = name
        self._year = year
        if artist is None:
            self._artist = Artist("Various Artists")
        else:
            _artist = artist

        self._tracks = []

    def add_song(self, song, position=None):
        if position is None:
            self._tracks.append(song)
        else:
            self.tracks.insert(position, song)

class Artist:

    def __init__(self, name):
        self._name = name
        self._albums = []

    def add_album(self, album):
        self._albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)


if __name__ == '__main__':
    load_data()

