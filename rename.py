import os
import glob
import sys
import re

path = "."
files = os.listdir(path)
current_index = 0

def get_newfile(files):
    global list_old 
    list_old = []
    global list_new 
    list_new = []

    for index, file in enumerate(files):
    #    print(file) 
        if file.startswith('wall_'):
            list_old.append(file)
        else:
            list_new.append(file)

    print(list_new)
    return list_new

def write_newfile(files):
    global current_index
    for f in list_new:
        if f in ['rename.py', '.git' ]:
            continue
        else:
            result = os.rename(f, 'wall_' + str(current_index)+ '.jpg')
            current_index = current_index+1

def current_count():
    global current_index
    wall_list = []
    for name in glob.glob('wall_*'):
        short_name = int(name[5:-4])
        wall_list.append(short_name)
        wall_list.sort()
    current_index = wall_list[-1]+1
    print(current_index)
    return current_index

if __name__ == '__main__':
    current_count()
    get_newfile(files)
    write_newfile(files)
