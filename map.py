text = "what is the best team in the world"


def corp_caps():
    capitals = [char.upper() for char in text]
    return capitals
    
def map_caps():
    map_capitals = list(map(str.upper, text))
    return map_capitals


map_words = list(map(str.upper, text.split(' ')))
print(map_words)

for x in map(str.upper, text.split(' ' )):
    print(x)
    
if __name__ == '__main__':
    print(corp_caps())
    print(map_caps())
