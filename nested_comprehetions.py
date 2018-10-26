burgers = ["beef", "chicken", "spicy bean"]
topings = ["cheese", "eggs", "beans", "span"]

meals = [{burger, toping} for burger in burgers for toping in topings]
print(meals)

for burger in burgers:
    for toping in topings:
        print((burger, toping))
        
for meals in [{burger, toping} for burger in burgers for toping in topings]:
    print(meals)
    
for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)

times = ({i, i * j} for i in range(1, 11) for j in range(1, 11))
print(times)    
