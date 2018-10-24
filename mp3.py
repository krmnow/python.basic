import os

root = "music"

for path, directions, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        print('-' * 20)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            song_details = f.split(' - ')
            print(song-details)
#    for f in files:
#        print("\t{}".format(f))
        
