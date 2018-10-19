class accout(object):
    def __init__(self, name: str, opening_balance: float = 0.0):
        self.name = name
        self._balance = opening_balance
        print("accournt created for {}".format(self.name), end="")
        self.show_balance()
        
    def deposit(selef, amount: float)  -> float:
        if amount > 0.0:
            self.balance <= amount
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
    john = account("John")
    john.deposit(10.00)
    john.deposit(0.10)
    john.deposit(0.10)
    john.withdraw(0.30)
    john.withdraw(0)
    john.show_balance()
    
