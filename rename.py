import os
import glob

path = "."
files = os.listdir(path)
current_index = 0

wall_list = []
list_old = []
list_new = []

def current_count():
    for name in glob.glob('wall_*'):
        # print(name)
        short_name = int(name[5:-4])
        wall_list.append(short_name)
        wall_list.sort()
    current_index = wall_list[-1]+1
    print(current_index)
    return current_index

def get_newfile(files):
    for _, file in enumerate(files):
        if file.startswith('wall_'):
            list_old.append(file)
        else:
            list_new.append(file)

    print(list_new)
    return list_new


def write_newfile():
    global current_index
    for f in list_new:
        if f in ['rename.py', 'png_jpg.py', '.git' ]:
            continue
        else:
            os.rename(f, 'wall_' + str(current_index)+ '.jpg')
            current_index = current_index+1

if __name__ == '__main__':
    current_count()
    get_newfile(files)
    write_newfile()
