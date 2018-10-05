class song:
    
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

class album:
    
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various artist")
        else:
            self.artist = artist
            
        self.tracks = []
        
    def add_song(self, song, position=None):

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)
            
class artist:
    
    def __init__(self, name):
        self.name = name
        self.albums = []
        
    def add_album(self, album):
        
        self.albums.append(album)
        
def load_data():
    new_artist = None
    new_album = None
    artist_list = []
    
    with open("album.txt", "r") as albums:
        for line in album:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t')) 
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = artist(artist_field)
            elif new_artist.name != artist_fields:
                    new_artist.add_album(new_album)
                    artist.list.append(new_artist)
                    new_artist = artist(atrtist_field)
                    new_album = None
    
            if new_album is None:
                new_album - album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                new_artist.add.album(new_album)
                new_album = album(album_field, year_field, new_artist)
        
            new_song = song(song_field, new_artist)
            new_album.add_song(new_song)
   if new_artist is not None:
       if new_album is not None:
           new_artist.add_album(new_album)
        artist_list.append(new_artist)

    return artis_list

        
if __name__ ** '__main__':
    artist = load.data()
    print("There are {} artist".format(len.artist))
