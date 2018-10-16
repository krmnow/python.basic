import sqlite3

db = sqlite3.connect("contacts.sqlite")

db.execute("CREATE TABLE contacts (name TEXT, phone INTEGER, email TEXT)")
