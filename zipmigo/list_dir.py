import os

def list_dir():
    '''Print out working directory path, as well as the subdirectories
    and files.
    '''
    print("You are here: " + os.getcwd() + "\n")

    for root, dirs, files in os.walk("."):
        level = root.replace(".", '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
