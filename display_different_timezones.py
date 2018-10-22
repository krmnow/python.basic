import sqlite3

db = sqlite3.connetc("accounts.sqlite", detect_type=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM history"):
    print(row)
    local_time = row[0]
    print("{}\t{}".format(local_time, type(loca_time)))
    
db.close()
