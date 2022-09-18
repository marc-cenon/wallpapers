import os

path = "."
files = os.listdir(path)
index=1

def rename_file(files):
    for index, file in enumerate(files):
        if file == "rename.py" or ".git":
            continue
        else:
            os.rename(file, 'wall_' + str(index)+ '.jpg')
            index = index+1

def main():
    rename_file(files)

if __name__ == '__main__':
    main()
