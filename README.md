# CartoonGAN - Generate dataset

With this script I generate the dataset for my implementation of the cartoon GAN [1]. In the original paper, the data was produced by extracting images from anime movies, e.g. the movie "Spirited Away"  by Miyazaki Hayao.

Due to copyright reasons I tried to find an alternative dataset, which I have found in the safebooru [2] dataset from kaggle. Problem of this procedure are the different creators and their different styles of the images. This will not train the network properly I think, but I give it a try. In the paper, only one style from one artist is used.

- download `all_data.csv` from safebooru dataset
- configure path of this file in `PATH_TO_SAFEBOORU_ALL_DATA_CSV`
- configure where to store images in `PATH_TO_STORE_DOWNLOADED_IMAGES`
- run `image_downloader.py` to download first 1.000 medium size images

[1] https://s3.amazonaws.com/video.udacity-data.com/topher/2018/November/5bea23cd_cartoongan/cartoongan.pdf

[2] https://www.kaggle.com/alamson/safebooru