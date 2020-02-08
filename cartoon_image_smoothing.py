import os
import cv2
from PIL import Image, ImageFilter
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
        cartoon_images_filename = PATH_TO_STORED_CARTOON_IMAGES + filename
        smoothed_images_filename = PATH_TO_STORE_SMOOTHED_IMAGES + filename

        if not os.path.exists(smoothed_images_filename):
            edge_smoothing(cartoon_images_filename, smoothed_images_filename)
        else:
            print("Skipping file, already exists, ", cartoon_images_filename)

    downloader.zip_images(SMOOTHED_IMAGES_ZIPFILE_NAME, PATH_TO_STORE_SMOOTHED_IMAGES)

def edge_smoothing(cartoon_images_filename, smoothed_images_filename):
    print("Edge-smoothing of ", cartoon_images_filename)
    origin = cv2.imread(cartoon_images_filename)
    edges = createEdgesOverlay(origin)
    result = overlayEdges(edges, origin)
    result.save(smoothed_images_filename, "JPEG")

def overlayEdges(edges, origin):
    background = transformFromCV2ToPillowImageFormat(origin)
    background.paste(edges, (0, 0), edges)
    background = background.convert("RGB")
    return background

def transformFromCV2ToPillowImageFormat(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    return Image.fromarray(img)

def createEdgesOverlay(origin):
    edges = cv2.Canny(origin, 30, 300, 3)
    edges = cv2.dilate(edges, (3, 3))
    edges = cv2.bitwise_not(edges)
    edges = transformFromCV2ToPillowImageFormat(edges)
    makeWhiteBackgroundTransparent(edges)
    edges = edges.filter(ImageFilter.GaussianBlur) #do blurring here because doing it before making background transparent results in white halo

    return edges

# got this from here:
# https://stackoverflow.com/questions/765736/using-pil-to-make-all-white-pixels-transparent/4531395
def makeWhiteBackgroundTransparent(img):
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)

if __name__ == '__main__':
    main()