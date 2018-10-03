import datetime
import pytz



class account:
    
    @staticmethod    
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [account._current_time(), balance]
        print("Account cerated for " + self.name)
        self.show_balance()
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append(account._current_time(), amount)
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append(account._current_time(), -amount)
        else:
            print("Amount must be graeater than zero")
        self.show_balance
    def show_balance(self):
        print("Balance is {}".format(self.balance))
        
    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{6} {} on {} (local time was) {}".format(amount, tran_type, date, date.astimezone()))

if __name__ == '__main__':
    tin = account("Tin", 0)
    tin.show_balance()
    
tin.deposit(1000)
   # tin.show_balance()
tin.withdraw(500)
   # tin.show_balance()
tin.withdraw(500)

tin.show_transactions()

steph = account("steph", 800)
steph.deposit(100)
steph.withdraw(200)
steph.show_transactions()
