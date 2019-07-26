import os
import shutil
import urllib.request

def init_counter(path_to_count_content):
    if not os.path.exists(path_to_count_content):
        return 0
    else:
        already_existing_no_of_files = len(os.listdir(path_to_count_content))
        print("Already downloaded files: ", already_existing_no_of_files)
        return already_existing_no_of_files

def download_non_already_existing_images(filename_with_path, url):
    if not os.path.exists(filename_with_path):
        return download_image(url, filename_with_path)
    else:
        print("Skipping file, already exists: ", filename_with_path)
        return False

def download_image(url, filename):
    try:
        with urllib.request.urlopen(url) as response, open(filename, 'wb') as saving_file:
            shutil.copyfileobj(response, saving_file)
            return True
    except urllib.error.HTTPError as e:
        print(e)
        return False

def zip_images(zipfile_name, path_to_data_to_be_zipped):
    shutil.make_archive(zipfile_name, 'zip', path_to_data_to_be_zipped)