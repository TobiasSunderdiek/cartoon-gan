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
`- run `cartoon_image_downloader.py` to download configurable amount of medium size images

### Edge-smoothed version of cartoon images

To make the GAN better learn to produce clear edges in the cartoon image, the model is trained with an edge-smoothed version on every cartoon image, too. In the paper, the edges are first detected by canny-edge, then the edges are dilated and smoothed with gaussian smoothing. I failed to combine the canny edged version of the image with the original version, so I just gaussian smoothed the whole image. My approach may result in bad output images, but I give it a try.

With the script `cartoon_image_smoothing.py` I create a gaussian smoothed version of every cartoon image.

- use downloaded images from safebooru as described above
- configure where the cartoon images are stored in `PATH_TO_STORED_CARTOON_IMAGES`
- configure where to store smoothed images in `PATH_TO_STORE_SMOOTHED_IMAGES`
- `pip install opencv-python`
- configure where to store resulting .zip-file of images in `SMOOTHED_IMAGES_ZIPFILE_NAME`
- run `cartoon_image_smoothing.py` to create the images

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

\[1\] http://openaccess.thecvf.com/content_cvpr_2018/papers/Chen_CartoonGAN_Generative_Adversarial_CVPR_2018_paper.pdf

\[2\] https://www.kaggle.com/alamson/safebooru

\[3\] http://cocodataset.org

\[4\] https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocoDemo.ipynb

\[5\] http://images.cocodataset.org/annotations/annotations_trainval2017.zip