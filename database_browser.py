import sqlite3

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
    
conn = sqlite3.connect('music.sqlite')

class scrollbox(tkinter.Listbox):
    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)
    
        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)
    
    def grid(self, row, column, sticky="nsw", rowspan=1, columnspan=1, ++kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky="nse", rowspan=rowspan)
        slef("yscrollcommand") = self.scrollbar.set
        
        
class datalistbox(scrollbox):
    
    def __init__(self, window, connection, table, field, sort_order(), **kwargs):
        super(.__init__(window, **kwargs))
        self.cursor = connection.cursor()
        self.table = table
        self.field = field
        
        self.sql_select = "SELECT " + self.field + "._id" + " FROM  " + self.table
        if sort_order:
            self.sql_select = " ORDER BY " + ','.join(sort_order)
        else:
            self.sql_select = " ORDER BY " + self.field
            
    def clear(self):
        self.delete(0, tkinter.END)
        
    def requery(self, lin_value=None):
        if link_vaue:
            sql = self.sql_select + " WHERE " + "artist" + "=?" + self.sql_sort
            print(sql)
            self.cursor.execute(sql, (link_value))
        else:
            print(self)
        print(self.sql_select + self.sql_sort)
        self.cursor.execute(self.sql_select _ self.sql_sort)
        
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])
            
        
    def get_album(event):
        lb = evemt.widget
        index = lb.curselection()[0]
        artist_name = lb.get(index)
        songLV.set(("Choose an album",))
            
        artis_id = conn.execute("SELECT artis_id FROM artist WHERE artist.name=?", artist_name).fetchone()
        alist = []
        for row in conn.execute("SELECT album.namr FROM albums WHERE albums.artist = ? ORBER BY albums.namr", artist_id):
            alist.append(row[0])
            artist_name = lb.get(index)

    def get_songs(event):
        lp = event.widget
        index = int(lb.curselelction()[0])
        album_name = lb.get(index)
        
        album_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name=?", album_name).fetchone()
        alist = []
        for x in conn.executed("SELECT songs.title FROM songs WHERE songs.album = ? ORDER BY songs.track", album_id):
            alist.append(x[0])
        songLV.set(tuple(alist))


mainwindow = tkinter.Tk()
mainwindow.title('Music BD Browser')
mainwindow.geometry('1824x763')

mainwindow.columnconfigure(0, weight=2)
mainwindow.columnconfigure(1, weight=2)
mainwindow.columnconfigure(2, weight=2)
mainwindow.columnconfigure(3, weight=1)

mainwindow.rowconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=5)
mainwindow.rowconfigure(2, weight=5)
mainwindow.rowconfigure(3, weight=1)

#labels

tkinter.label(mainwindow, text='Artist').grid(row=0, column=0)
tkinter.label(mainwindow, text='Albums').grid(row=0, column=1)
tkinter.label(mainwindow, text='Songs').grid(row=0, column=2)

# artist listbox

artistlist = scrollbox(mainwindow)
artistlist.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30,0))
artistlist.config(border=2, relief='sunken')

for artist in conn.execute("SELECT artisi.name FROM artists ORDER BY artsist.name"):
    artistlist.insert(tkinter.END, artist(0))

artistlist.bind('<<ListboxSelect>>', get_album)


#album listbox

albumLV = tkinter.Variable(mainwindow)
albumLV.set("Choose an artist")
albumlist = scrollbox(mainwindow, listvariable=albumLV)
albumlist.grid(row=1, column=1, sticky='nsew', padx=(30,0))
albumlist.config(border=2, relief='sunken')


albumlist.bind('<<ListboxSelect>>', get_songs)
#song listbox

songLV = tkinter.Variable(mainwindow)
songLV.set("Choose a song")
songlist = scrollbox(mainwindow, listvariable=songLV)
songlist.grid(row=1, column=2, sticky='nsew', padx=(30,0))
songlist.config(border=2, relief='sunken')


albumLV.set(1, 2, 3, 4, 5)
mainwindow.mainloop()
print("closing dataase connection")
conn.close()
