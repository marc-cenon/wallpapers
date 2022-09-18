import os

path = "."
files = os.listdir(path)
index=1
        
for index, file in enumerate(files):
    if file == "rename.py":
        continue
    else:
        os.rename(file, 'wall_' + str(index)+ '.jpg')
        index = index+1
