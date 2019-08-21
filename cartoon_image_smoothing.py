import os
import cv2
import downloader

PATH_TO_STORED_CARTOON_IMAGES = './safebooru/'
PATH_TO_STORE_SMOOTHED_IMAGES = './safebooru_smoothed/'
SMOOTHED_IMAGES_ZIPFILE_NAME = './safebooru_smoothed'

def main():
    if not os.path.exists(PATH_TO_STORED_CARTOON_IMAGES):
        print("Can not smooth images, path does not exist: ", PATH_TO_STORED_CARTOON_IMAGES)

    if not os.path.exists(PATH_TO_STORE_SMOOTHED_IMAGES):
        os.makedirs(PATH_TO_STORE_SMOOTHED_IMAGES)

    for filename in os.listdir(PATH_TO_STORED_CARTOON_IMAGES):
        img = cv2.imread(PATH_TO_STORED_CARTOON_IMAGES+filename)
        blurred_img = cv2.GaussianBlur(img, (9, 9), 0)
        cv2.imwrite(PATH_TO_STORE_SMOOTHED_IMAGES+filename, blurred_img)
        break

    downloader.zip_images(SMOOTHED_IMAGES_ZIPFILE_NAME, PATH_TO_STORE_SMOOTHED_IMAGES)

if __name__ == '__main__':
    main()