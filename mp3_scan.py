import os
import fmatch

def find_music(starts, extension):
    for path, directories, files in os.walk(starts):
        for file in fmatch.filter(files, "*.{}".format(extension)):
            yield os.path.join(path, file)
            
for f in find_music("music", "mp3")
    print(f)            
