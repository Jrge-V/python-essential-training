import urllib.request
from urllib.error import HTTPError
import os


def download_files(first_file_path, folder):
    image_num = first_file_path[-7:-4]
    image_num = int(image_num)
    i = 1

    # check if folder exists, else create a new one
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_paths = first_file_path

    while True:
        try:
            print(image_num)
            urllib.request.urlopen(file_paths)
            file_name = os.path.join(folder, f'image{i}.jpg')
            i += 1

            urllib.request.urlretrieve(file_paths, file_name)

            image_num = int(image_num)
            image_num += 1
            if image_num < 10:
                image_num = ('00' + str(image_num))
            else:
                image_num = ('0' + str(image_num))

            file_paths = list(file_paths)
            file_paths[-7:-4] = image_num
            file_paths = ''.join(file_paths)

            print('found url')

        except HTTPError:
            print('HTTP ERROR: 404 invalid url')
            print(file_paths)
            break


# TEST CODE
download_files('https://699340.youcanlearnit.net/image001.jpg', 'images')
