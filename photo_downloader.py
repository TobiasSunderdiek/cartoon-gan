import os
from pycocotools.coco import COCO
import downloader
import config

PATH_TO_STORE_DOWNLOADED_PHOTOS = "./photos/"
PATH_TO_COCO_ANNOTATIONS_ROOT_FOLDER = "."
DATA_TYPE='train2017'
ANNOTATION_FILE = '{}/annotations/instances_{}.json'.format(PATH_TO_COCO_ANNOTATIONS_ROOT_FOLDER, DATA_TYPE)
PHOTO_ZIPFILE_NAME = './coco'

def main():
    if not os.path.exists(PATH_TO_STORE_DOWNLOADED_PHOTOS):
        os.makedirs(PATH_TO_STORE_DOWNLOADED_PHOTOS)

    coco = COCO(ANNOTATION_FILE)

    personCategory = coco.getCatIds(catNms=['person'])
    personImageIds = coco.getImgIds(catIds=personCategory)
    personImageData = coco.loadImgs(personImageIds)
    personImageDataIterator = iter(personImageData)

    counter = downloader.init_counter(PATH_TO_STORE_DOWNLOADED_PHOTOS)
    while counter <= config.COUNT_IMAGES_TO_DOWNLOAD:
        try:
            filename_with_path, url = get_filename_and_url(personImageDataIterator)
            success = downloader.download_non_already_existing_images(filename_with_path, url)
            if success:
                counter += 1
                print("Download #", counter)
        except StopIteration:
            print('Tried to download more photos than available, stopping.')
            counter = config.COUNT_IMAGES_TO_DOWNLOAD + 1
            pass
    downloader.zip_images(PHOTO_ZIPFILE_NAME, PATH_TO_STORE_DOWNLOADED_PHOTOS)

def get_filename_and_url(personImageDataIterator):
    photo_data = next(personImageDataIterator)
    url = photo_data['coco_url']
    filename = photo_data['file_name']
    filename_with_path = PATH_TO_STORE_DOWNLOADED_PHOTOS + filename

    return filename_with_path, url

if __name__ == '__main__':
    main()
