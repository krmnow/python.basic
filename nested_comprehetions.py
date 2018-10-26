burgers = ["beef", "chicken", "spicy bean"]
topings = ["cheese", "eggs", "beans", "span"]

meals = [{burger, toping} for burger in burgers for toping in topings]
print(meals)

for burger in burgers:
    for toping in topings:
        print((burger, toping))
        
for meals in [{burger, toping} for burger in burgers for toping in topings]
print(meals)
