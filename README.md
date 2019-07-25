# CartoonGAN - my try to implement it

Within this repo, I try to implement a cartoon GAN [1].

## Generate dataset

### Cartoon images

With the script `image_downloader.py` I get the cartoon part of the dataset for my implementation of the cartoon GAN. In the original paper, the data was produced by extracting images from anime movies, e.g. the movie "Spirited Away"  by Miyazaki Hayao.

Due to copyright reasons I tried to find an alternative dataset, which I have found in the safebooru [2] dataset from kaggle. Problem of this procedure are the different creators and their different styles of the images. This will not train the network properly I think, but I give it a try. In the paper, only one style from one artist is used.

- download `all_data.csv` from safebooru dataset
- configure path of this file in `PATH_TO_SAFEBOORU_ALL_DATA_CSV`
- configure where to store images in `PATH_TO_STORE_DOWNLOADED_IMAGES`
- configure where to store resulting .zip-file of images in `IMAGES_ZIPFILE_NAME`
- run `image_downloader.py` to download configurable amount of medium size images

### Photos

In the paper, photos are downloaded from flickr. In my implementation I try to use the COCO[3] dataset.

[1] https://s3.amazonaws.com/video.udacity-data.com/topher/2018/November/5bea23cd_cartoongan/cartoongan.pdf

[2] https://www.kaggle.com/alamson/safebooru

[3] http://cocodataset.org