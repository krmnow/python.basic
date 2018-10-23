import sqlite3

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
    
conn = sqlite3.connect('music.sqlite')

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

artistlist = tkinter.Listbox(mainwindow)
artistlist.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30,0))
artistlist.config(border=2, relief='sunken')

#album listbox

albumLV = tkinter.Variable(mainwindow)
albumLV.set("Choose an artist")
albumlist = tkinter.Listbox(mainwindow, listvariable=albumLV)
albumlist.grid(row=1, column=1, sticky='nsew', padx=(30,0))
albumlist.config(border=2, relief='sunken')

#song listbox

songLV = tkinter.Variable(mainwindow)
songLV.set("Choose a song")
songlist = tkinter.Listbox(mainwindow, listvariable=songLv)
songlist.grid(row=1, column=2, sticky='nsew', padx=(30,0))
songlist.config(border=2, relief='sunken')

mainwindow.mainloop()
print("closing dataase connection")
conn.close()
