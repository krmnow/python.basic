from data import people, basic_plants_list, plants_list

people = []

if  bool(people) and all([person[1] for person in people]):
    print("sending email")
else:
    print("user must edit the list of reciptiens")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")
else:
print("No grasses in this plack")    

if any(plant.plant_type == "Grass" for plant in plans_dict.values()):
    print("The dict contain grasess")
else:
    print("No grasses in the dict")
