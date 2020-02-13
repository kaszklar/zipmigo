import requests
from zipfile import ZipFile
from tqdm import tqdm
import os

def download(url, name):
    '''Download a zipfile from http URL to current directory; print out status.

    Response Codes
    --------------
    200 = good, 403 = blocked, 404 = not found

    Arguments
    ---------
    url : string
    name: string, must contain file extension. no spaces or special characters.
    '''

    response = requests.get(url)

    if(response.status_code == 200):
        with open(name, 'wb') as handle:
            for chunk in tqdm(leave=False, iterable= response.iter_content(), \
             total = len(response.content)):
                handle.write(chunk)
        print("download complete")
    else:
        print("cannot download, status code: " + str(response.status_code))



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





def unzip(zfilename):
    '''Unzip a zip archive to the working directory.

    Place that archive in working dir if it is a root archive.
    Else, place in a subdirectory.

    Arguments
    ---------
    zfilename : string, name of zip file. Must contain the .zip extension.
    '''

    zdir = zfilename.split('.')[-2]

    file = ZipFile(zfilename, "r")

    #pull out the filenames from the archive
    filez = []
    for info in file.infolist():
        filez.append(info.filename)

    #if all files are in subdirectories, unzip to current dir
    if all(["/" in s for s in filez]):
        with ZipFile(zfilename) as myzip:
            myzip.extractall(".")
            print("successfully unzipped to current directory")
    #else, at least one file located at root of archive; unzip to dir
    else:
        with ZipFile(zfilename) as myzip:
            myzip.extractall(zdir)
            print("successfully unzipped to " + zdir +"/")
