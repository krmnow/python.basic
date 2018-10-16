import sqlite3

db = sqlite3.connect("contacts.sqlite")

db.execute("CREATE TABLE contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES ('Tim', 43354252, 'email@email.pl')")
db.execute("INSERT INTO contacts VALUES ('Ida', 5435, 'myemail@gmail.pl')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

print(cursor.fetchall())

for row in cursor:
    print(row)

cursor.close()
db.close()

