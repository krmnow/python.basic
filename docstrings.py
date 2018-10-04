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
            
