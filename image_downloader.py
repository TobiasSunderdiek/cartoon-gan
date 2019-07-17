import urllib.request
import shutil
import os

PATH_TO_SAFEBOORU_ALL_DATA_CSV = '/Users/ts/Downloads/all_data.csv'
PATH_TO_STORE_DOWNLOADED_IMAGES = '/Users/ts/Download/safebooru/'
COUNT_IMAGES_TO_DOWNLOAD = 1000

def main():
    if not os.path.exists(PATH_TO_STORE_DOWNLOADED_IMAGES):
        os.makedirs(PATH_TO_STORE_DOWNLOADED_IMAGES)

    with open(PATH_TO_SAFEBOORU_ALL_DATA_CSV) as raw_data:
        raw_data.readline() # ignore header line by reading it
        counter = 1
        while counter <= COUNT_IMAGES_TO_DOWNLOAD:
            success = fetch_and_save_image(raw_data.readline())
            if success:
                counter += 1
                print('Download #', counter)

def fetch_and_save_image(raw_data_line):
    url = get_image_url(raw_data_line)
    filename_with_path = get_filename_with_path(url)
    return download_image(url, filename_with_path)

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
        return False

if __name__ == '__main__':
    main()