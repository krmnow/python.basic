text = "what is the best team in the world"


map_capitals = list(map(str.upper, text))
print(map_capitals)

map_words = list(map(str.upper, text.split(' ')))
print(map_words)
