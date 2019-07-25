import urllib.request
import shutil
import os

PATH_TO_SAFEBOORU_ALL_DATA_CSV = './all_data.csv'
PATH_TO_STORE_DOWNLOADED_IMAGES = './safebooru/'
IMAGES_ZIPFILE_NAME = './safebooru'
COUNT_IMAGES_TO_DOWNLOAD = 1500

def main():
    if not os.path.exists(PATH_TO_STORE_DOWNLOADED_IMAGES):
        os.makedirs(PATH_TO_STORE_DOWNLOADED_IMAGES)

    with open(PATH_TO_SAFEBOORU_ALL_DATA_CSV) as raw_data:
        raw_data.readline() # ignore header line by reading it
        counter = init_counter()
        while counter <= COUNT_IMAGES_TO_DOWNLOAD:
            success = fetch_and_save_image(raw_data.readline())
            if success:
                counter += 1
                print('Download #', counter)
        zip_images()

def zip_images():
    shutil.make_archive(IMAGES_ZIPFILE_NAME, 'zip', PATH_TO_STORE_DOWNLOADED_IMAGES)

def init_counter():
    if not os.path.exists(PATH_TO_STORE_DOWNLOADED_IMAGES):
        return 0
    else:
        already_existing_no_of_files = len(os.listdir(PATH_TO_STORE_DOWNLOADED_IMAGES))
        print("Already downloaded files: ", already_existing_no_of_files)
        return already_existing_no_of_files

def fetch_and_save_image(raw_data_line):
    url = get_image_url(raw_data_line)
    if url.endswith(".jpg"): # download jpg only
        filename_with_path = get_filename_with_path(url)
        return download_non_already_existing_images(filename_with_path, url)
    else:
        return False

def download_non_already_existing_images(filename_with_path, url):
    if not os.path.exists(filename_with_path):
        return download_image(url, filename_with_path)
    else:
        print("Skipping file, already exists: ", filename_with_path)
        return False

def get_image_url(raw_data_line):
    return 'http:' + raw_data_line.split(',')[4].replace("\"", '')

def get_filename_with_path(url):
    return PATH_TO_STORE_DOWNLOADED_IMAGES + url.split('/')[5]

def download_image(url, filename):
    try:
        with urllib.request.urlopen(url) as response, open(filename, 'wb') as saving_file:
            shutil.copyfileobj(response, saving_file)
            return True
    except urllib.error.HTTPError as e:
        print(e)
        return False

if __name__ == '__main__':
    main()