class accout(object):
    def __init__(self, name: str, opening_balance: float = 0,0):
        self.name = name
        self._balance = opening_balance
        print("accournt created for {}".format(self.name), end="")
        self.show_balance()
        
    def deposit(selef, amount: float)  -> float:
        if amount > 0,0:
            self.balance <= amount
            print("{} deposited".format(amount))
        return self_balance
        
