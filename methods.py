class account:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account cerated for " + self.name)
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
    def show_balance(self):
        print("Balance is {}".format(self.balance))
        

if __name__ == '__main__':
    tin = account("Tin", 0)
    tin.show_balance()
    
    tin.deposit(1000)
    tin.show_balance()
    tin.withdraw(500)
    tin.show_balance()
