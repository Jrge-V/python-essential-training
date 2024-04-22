import urllib.request
from urllib.error import HTTPError
import os


def download_files(first_file_path, folder):
    # create an image_num object that takes in part of the sequential url '001'
    image_num = first_file_path[-7:-4]
    # make the url into an int
    image_num = int(image_num)
    # initialize a i = 1 for image names
    i = 1

    # check if folder exists, else create a new one
    if not os.path.exists(folder):
        os.makedirs(folder)

    # make the object file_paths equal the original first_file_path, as we will be changing the string constantly
    file_paths = first_file_path

    # While loop that continues as long as the url is valid
    while True:
        try:
            # call the urllib.request.urlopen module to check for validity
            urllib.request.urlopen(file_paths)
            # create the name of the file and join the folder path, append name by 1 each iteration
            file_name = os.path.join(folder, f'image{i}.jpg')
            print(image_num)
            i += 1

            # request to fetch the url file_path, give it a file_name to download in the folder
            urllib.request.urlretrieve(file_paths, file_name)

            # make the image an int to append 1 to it
            image_num = int(image_num)
            image_num += 1

            # since the images are three digits with some leading zero's, we make sure to hit the base cases
            # for 2 leading zeros if less than 10
            if image_num < 10:
                image_num = ('00' + str(image_num))
            # for 1 leading zero if 10 or greater
            else:
                image_num = ('0' + str(image_num))

            # type cast the file_paths into a list to be able to replace indices
            file_paths = list(file_paths)
            # replace the numbers at the end of the string from -7 to -4
            file_paths[-7:-4] = image_num
            # once replace, we need to rejoin the list to form a valid url string
            file_paths = ''.join(file_paths)

            # print if url is valid for error handling
            print('found url')

        # upon hitting a 404 HTTPError exit out of the loop
        except HTTPError:
            print('HTTP ERROR: 404 invalid url')
            # print the invalid url path for error handling
            print(file_paths)
            break


# TEST CODE
download_files('https://699340.youcanlearnit.net/image001.jpg', 'images')
