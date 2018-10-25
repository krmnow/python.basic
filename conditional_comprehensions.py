menu = [
        ["eggs", "pasta", "pizza"],
        ["eggs", "sausage", "bacon"],
        ["eggs", "sudo", "small sous"],
        ["spam", "bacon", "bacon", "span"],
        ["chicken", "chips"]
        ]
meals = []

for meal in menu:
    if "span" not in meal:
        meals.append(meal)
    else:
         meals.append("a neal was skipped")
print(meals)

meals = [meal for meal in menu if "spam" not in meal]
print(meals)

x= 12
expresions = "tweleve" if x == 12 else "unknow"
print(expresions)

for meal in menu:
    print(meal, "contains chicken" if "chicken" in meal else "contains bacon" if "bacon" in meal else "contains eggs" )
