# CartoonGAN - my attempt to implement it

Within this repo, I try to implement a cartoon GAN \[1\].

## Generate dataset

`pip install -r requirements.txt`
### Cartoon images

With the script `cartoon_image_downloader.py` I get the cartoon part of the dataset for my implementation of the cartoon GAN. In the original paper, the data was produced by extracting images from anime movies, e.g. the movie "Spirited Away"  by Miyazaki Hayao.

Due to copyright reasons I tried to find an alternative dataset, which I have found in the safebooru [2] dataset from kaggle. Problem of this procedure are the different creators and their different styles of the images. This will not train the network properly I think, but I give it a try. In the paper, only one style from one artist is used.

- download `all_data.csv` from safebooru dataset [here](https://www.kaggle.com/alamson/safebooru/download)
- point to `all_data.csv` in `PATH_TO_SAFEBOORU_ALL_DATA_CSV` of `cartoon_image_downloader.py`
- configure the folder where you want the script to download the images to in `PATH_TO_STORE_DOWNLOADED_CARTOON_IMAGES`
- the script creates a .zip-file of the downloaded images, configure path where to store resulting .zip-file in `CARTOON_IMAGES_ZIPFILE_NAME`
- run `cartoon_image_downloader.py` to download configurable amount of medium size images

### Edge-smoothed version of cartoon images

To make the GAN better learn to produce clear edges in the cartoon image, the model is trained with an edge-smoothed version on every cartoon image, too. In the paper, the edges are first detected by canny-edge, then the edges are dilated and smoothed with gaussian smoothing.
In my implementation, I do the canny edges, the dilation and the gaussian blur with openCV and I make the white backbground transparent and paste the edges back on the original image with Pillow.

With the script `cartoon_image_smoothing.py` I create a edge-smoothed version of every cartoon image.

- use downloaded images from safebooru as described above
- configure where the cartoon images are stored in `PATH_TO_STORED_CARTOON_IMAGES`
- configure where to store smoothed images in `PATH_TO_STORE_SMOOTHED_IMAGES`
- configure where to store resulting .zip-file of images in `SMOOTHED_IMAGES_ZIPFILE_NAME`
- run `cartoon_image_smoothing.py` to create the images

### Photos

In the paper, photos are downloaded from flickr. In my implementation I try to use the COCO\[3\] dataset, especially the category *person*.

With the script `photo_downloader.py` I get the photo part of the dataset, following the COCO part as described in \[4\].

- download and unzip coco annotations from \[5\]
- configure annotations dir location in `PATH_TO_COCO_ANNOTATIONS_ROOT_FOLDER`
- configure where to store photos in `PATH_TO_STORE_DOWNLOADED_PHOTOS`
- configure where to store resulting .zip-file of images in `PHOTO_ZIPFILE_NAME`
- run `photo_downloader.py` to download configurable amount of photos of persons

## Create and train model

All the steps are described in a [jupyter notebook, please see here for details](https://github.com/TobiasSunderdiek/cartoon-gan/blob/master/CartoonGAN.ipynb).

\[1\] http://openaccess.thecvf.com/content_cvpr_2018/papers/Chen_CartoonGAN_Generative_Adversarial_CVPR_2018_paper.pdf

\[2\] https://www.kaggle.com/alamson/safebooru

\[3\] http://cocodataset.org

\[4\] https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocoDemo.ipynb

\[5\] http://images.cocodataset.org/annotations/annotations_trainval2017.zip
