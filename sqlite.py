import sqlite3

db = sqlite3.connect("contacts.sqlite")

db.execute("CREATE TABLE contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO concats(name, phone, email) VALUES ('Tim', 43354252, 'email@email.pl')")
