import sqlite3

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
    
conn = sqlite3.connect('music.sqlite')
