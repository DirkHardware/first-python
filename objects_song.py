class Song:

    def __init__(self, title, artist, duration=0):

        self.title = title
        self.artist = artist
        self.duration = duration


class Album:

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):

        # if no position value is given to override the default value
        # it is pushed to the end of the list
        if position is None:
            self.tracks.append(song)
        # If a position value is given, it inserts it at the index point
        # given by the position value
        else:
            self.tracks.insert(position, song)


class Artist:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to he list.

        Args:
            album(Album): Album object to add to the list.
                If the album is already present, it will not be added again.
        """

        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                # We've just read details for a new artist
                # Store the current album in the current artists collection and create a new artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # We've just read a new album for the current artist
                # Store the current album in the artist's collection and create a new album object
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            # create new song object and add it to the current albums collection

            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # After reading the last line in the text file, we will have an artist and album that haven't been stored
        # Process them now
            if new_artist is not None:
                if new_album is not None:
                    new_artist.add_album(new_album)
                artist_list.append(new_artist)
    return artist_list


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists.".format(len(artists)))