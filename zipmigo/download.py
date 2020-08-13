import requests
from tqdm import tqdm

def download(url, loc_name):
    '''Download a zipfile from http URL to current directory; print out status.

    Most Common Response Codes
    --------------
    200 = good, 403 = blocked, 404 = not found

    Arguments
    ---------
    url : string
    loc_name: string for local filename, must contain file extension.
              no spaces or special characters.

    '''

    assert type(url) is str, "url is not a string: %r" % url
    assert type(loc_name) is str, "loc_name is not a string: %r" % loc_name
    assert url[-3:] == 'zip', "url is not a .zip: %r" % url
    assert loc_name[-3:] == 'zip', "loc_name missing .zip extension: %r" % loc_name
    assert " " not in loc_name, "loc_name contains spaces: %r" % loc_name

    response = requests.get(url)

    if response.status_code != 200:
        print("issue reaching url " + url)
        print("response status code: {}".format(response.status_code))

    if response.status_code == 200:
        try:
            with open(loc_name, 'wb') as handle:
                for chunk in tqdm(leave=False, iterable= response.iter_content(), \
                 total = len(response.content)):
                    handle.write(chunk)
            print("download complete")
        except:
            print("cannot download. status code " + str(response.status_code))
