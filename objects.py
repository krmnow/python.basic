class Kettl(object):
    
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False
        
keywood = Kettl("Keywood", 8.99)
print(keywood.make)
print(keywood.price)

keywood.price = 12.75
print(keywood.price)

hamilton = Kettl("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(keywood.make, keywood.price, hamilton.make, hamilton.price))
