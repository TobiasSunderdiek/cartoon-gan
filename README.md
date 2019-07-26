# CartoonGAN - my try to implement it

Within this repo, I try to implement a cartoon GAN \[1\].

## Generate dataset

### Cartoon images

With the script `cartoon_image_downloader.py` I get the cartoon part of the dataset for my implementation of the cartoon GAN. In the original paper, the data was produced by extracting images from anime movies, e.g. the movie "Spirited Away"  by Miyazaki Hayao.

Due to copyright reasons I tried to find an alternative dataset, which I have found in the safebooru [2] dataset from kaggle. Problem of this procedure are the different creators and their different styles of the images. This will not train the network properly I think, but I give it a try. In the paper, only one style from one artist is used.

- download `all_data.csv` from safebooru dataset
- configure path of this file in `PATH_TO_SAFEBOORU_ALL_DATA_CSV`
- configure where to store images in `PATH_TO_STORE_DOWNLOADED_CARTOON_IMAGES`
- configure where to store resulting .zip-file of images in `CARTOON_IMAGES_ZIPFILE_NAME`
- run `cartoon_image_downloader.py` to download configurable amount of medium size images

### Photos

In the paper, photos are downloaded from flickr. In my implementation I try to use the COCO\[3\] dataset, especially the category *person*.

With the script `photo_downloader.py` I get the photo part of the dataset, following the COCO part as described in \[4\].

- download and unzip coco annotations from \[5\]
- configure annotations dir location in `PATH_TO_COCO_ANNOTATIONS_ROOT_FOLDER`
- `pip install pycocotools`
- `pip install matplotlib`
- configure where to store photos in `PATH_TO_STORE_DOWNLOADED_PHOTOS`
- configure where to store resulting .zip-file of images in `PHOTO_ZIPFILE_NAME`
- run `photo_downloader.py` to download configurable amount of photos of persons

\[1\] https://s3.amazonaws.com/video.udacity-data.com/topher/2018/November/5bea23cd_cartoongan/cartoongan.pdf

\[2\] https://www.kaggle.com/alamson/safebooru

\[3\] http://cocodataset.org

\[4\] https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocoDemo.ipynb

\[5\] http://images.cocodataset.org/annotations/annotations_trainval2017.zip