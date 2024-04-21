import shutil
import os.path


def zip_all(inner_folder, allowed_extensions, export_zip):

    archived = shutil.make_archive(export_zip, 'zip', inner_folder)

    # if os.path.exists('E:/Zipped file.zip'):
    #     print(archived)
    # else:
    #     print("ZIP file not created")


zip_all('my_stuff', ['.csv', '.txt'], 'my_stuff.zip')
