import os
import config
import downloader

PATH_TO_SAFEBOORU_ALL_DATA_CSV = './all_data.csv'
PATH_TO_STORE_DOWNLOADED_CARTOON_IMAGES = './safebooru/'
CARTOON_IMAGES_ZIPFILE_NAME = './safebooru'

def main():
    if not os.path.exists(PATH_TO_STORE_DOWNLOADED_CARTOON_IMAGES):
        os.makedirs(PATH_TO_STORE_DOWNLOADED_CARTOON_IMAGES)

    with open(PATH_TO_SAFEBOORU_ALL_DATA_CSV) as raw_data:
        raw_data.readline() # ignore header line by reading it
        counter = downloader.init_counter(PATH_TO_STORE_DOWNLOADED_CARTOON_IMAGES)
        while counter <= config.COUNT_IMAGES_TO_DOWNLOAD:
            success = fetch_and_save_image(raw_data.readline())
            if success:
                counter += 1
                print('Download #', counter)
        downloader.zip_images(CARTOON_IMAGES_ZIPFILE_NAME, PATH_TO_STORE_DOWNLOADED_CARTOON_IMAGES)

def fetch_and_save_image(raw_data_line):
    url = get_image_url(raw_data_line)
    if url.endswith(".jpg"): # download jpg only
        filename_with_path = get_filename_with_path(url)
        return downloader.download_non_already_existing_images(filename_with_path, url)
    else:
        return False

def get_image_url(raw_data_line):
    return 'http:' + raw_data_line.split(',')[4].replace("\"", '')

def get_filename_with_path(url):
    return PATH_TO_STORE_DOWNLOADED_CARTOON_IMAGES + url.split('/')[5]

if __name__ == '__main__':
    main()