from zipfile import ZipFile

def unzip(zfilename):
    '''Unzip a zip archive to the working directory.

    Place that archive in working dir if it is a root archive.
    Else, place in a subdirectory.

    Arguments
    ---------
    zfilename : string, name of zip file. Must contain the .zip extension.
    '''

    assert type(zfilename) is str, "zfilename is not a string: %r" % zfilename
    assert zfilename[-3:] == 'zip', "zfilename is not a .zip: %r" % zfilename

    try:
        zdir = zfilename.split('.')[-2]

        file = ZipFile(zfilename, "r")
    except:
        print("no such file or unable to open " + zfilename)

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
