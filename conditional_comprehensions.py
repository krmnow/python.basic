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
print(meals)

meals = (meal for meal in menu if "span" in meal):
    print(meals)
