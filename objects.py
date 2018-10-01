class Kettl(object):
    
    power_source = "electricy"
    
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False
        
    def switch_on(self):
        self.on = True
        
keywood = Kettl("Keywood", 8.99)
print(keywood.make)
print(keywood.price)

keywood.price = 12.75
print(keywood.price)

hamilton = Kettl("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(keywood.make, keywood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(keywood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettl.switch_on(keywood)
print(keywood.on)
keywood.switch_on()

print("*" * 20)
keywood.power = 1.5
#print(keywood.power)

print("Switch to atomic power")
Kettl.power_source = "atomic"
print(Kettl.power_source)
print(keywood.power_source)
print(hamilton.power_source)

print(keywood.__dict__)
print(Kettl.__dict__)
print(hamilton.__dict__)
