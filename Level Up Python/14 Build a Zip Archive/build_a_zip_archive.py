from zipfile import ZipFile
import os


def zip_all(inner_folder, allowed_extensions, export_zip):

    # Open a new zip file for writing, passing in the name of the exported zip folder
    with ZipFile(export_zip, 'w') as zip_object:
        # walk through the directory tree using os.walk module searching for folder names, sub folders, and file names
        for foldername, subfolder, filenames in os.walk(inner_folder):
            # iterate over the files in current folder
            for filename in filenames:
                # iterate through extension listed in my allowed_extensions list
                for extension in allowed_extensions:
                    # if the extension ends with .csv or .txt
                    if filename.endswith(extension):
                        # get the full path of the file searching the folders
                        file_path = os.path.join(foldername, filename)
                        # write the file path to the zip archive, preserving relative path
                        zip_object.write(file_path, os.path.relpath(file_path, inner_folder))


# TEST CODE
zip_all('my_stuff', ['.csv', '.txt'], 'my_stuff.zip')
