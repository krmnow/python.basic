import sqlite3

db = sqlite3.connect("contacs.sqlite")

new_email = 'anotheremail@email.pl'
phone = input("Please enter phone number")

#update_sql = "UPDATE contacts SET email = '{}' where phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
print(update_sql)


update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} row update".format(update_cursor.connection == db))

print()
print("Are connection the same: {}".format(update_cursor.connection == db))

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)
    
db.close()
