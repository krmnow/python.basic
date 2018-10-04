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
