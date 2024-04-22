import urllib.request
from urllib.error import HTTPError
import os


def download_files(first_file_path, folder):

    # check if folder exists, else create a new one
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_paths = first_file_path

    for path in file_paths:
        try:
            urllib.request.urlopen(path)
            print('found url')
        except HTTPError:
            print('invalid url')




    # file_name = os.path.join(folder, 'image1' + '.jpg')
    # urllib.request.urlretrieve(file_path, file_name)



    # TODO: figure out how to download multiples images
    # TODO: Figure out how to sequentially add a +1 to the end of the url string for 50 files
    # pass


# TEST CODE
download_files('https://699340.youcanlearnit.net/image001.jpg', 'images')
