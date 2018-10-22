import sqlite3

db = sqlite3.connect('account.sqlite')
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS transactions (time TIMESTAMP NOT NULL,"
           " account TEXT NOT NULL amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class accout(object):
    def __init__(self, name: str, opening_balance: float = 0.0):
        cursor = db.execute("SELECT name, balance FRON accoubts WHERE (name = ?", (name),)
        row = cursor.fetchone()
        
        if row is not None:
            self.name, self._balance = row
            print("Retrived record for {}".format(self.name), end="")
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
        self.show_balance()
            
        self.name = name
        self._balance = opening_balance
        print("accournt created for {}".format(self.name), end="")
        self.show_balance()
        
    def deposit(selef, amount: float)  -> float:
        if amount > 0.0:
            new_balance = self._balance + amount
            deposite_time = pytz.utc.localize(datetime.datetime.utcnow())
            db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", new_balance, self.name)
            print("{} deposited".format(amount))
        return self_balance
        
    def withdraw(self, amount: float) -> float:
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("{} withdraw.".format(amount))
            return amount
        else:
            print("The amount must be greater than zero")
            return 0,0
    def show_balance(self):
        print("Balcne onm account {} is {}.".format(self.name, self._balance))
        
if __name__ == '__main__':
    john = accout("John")
    john.deposit(10.00)
    john.deposit(0.10)
    john.deposit(0.10)
    john.withdraw(0.30)
    john.withdraw(0)
    john.show_balance()
    
    terry = accout("TerryJ")
    gratan = accout("Gratan")
