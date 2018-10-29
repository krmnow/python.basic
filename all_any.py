from data import people, basic_plants_list, plants_list

people = []

if  bool(people) and all([person[1] for person in people]):
    print("sending email")
else:
    print("user must edit the list of reciptiens")
