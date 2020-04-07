# CartoonGAN - my attempt to implement it

Within this repo, I try to implement a cartoon GAN \[1\].

Full description and more details can be found here: https://tobiassunderdiek.github.io/cartoon-gan/

## Generate dataset

### Cartoon images

- download `all_data.csv` from safebooru dataset [here](https://www.kaggle.com/alamson/safebooru/download)
- point to `all_data.csv` in `PATH_TO_SAFEBOORU_ALL_DATA_CSV` of `cartoon_image_downloader.py`
- configure the folder where you want the script to download the images to in `PATH_TO_STORE_DOWNLOADED_CARTOON_IMAGES`
- the script creates a .zip-file of the downloaded images, configure path where to store resulting .zip-file in `CARTOON_IMAGES_ZIPFILE_NAME`
- run `make install` to install necessary libraries
- run `make cartoons` to download configurable amount of medium size images

### Edge-smoothed version of cartoon images

- use downloaded images from safebooru as described above
- configure where the cartoon images are stored in `PATH_TO_STORED_CARTOON_IMAGES`
- configure where to store smoothed images in `PATH_TO_STORE_SMOOTHED_IMAGES`
- configure where to store resulting .zip-file of images in `SMOOTHED_IMAGES_ZIPFILE_NAME`
- run `make cartoons-smooth` to create the images

### Photos

- download and unzip coco annotations from \[5\]
- configure annotations dir location in `PATH_TO_COCO_ANNOTATIONS_ROOT_FOLDER`
- configure where to store photos in `PATH_TO_STORE_DOWNLOADED_PHOTOS`
- configure where to store resulting .zip-file of images in `PHOTO_ZIPFILE_NAME`
- run `make photos` to download configurable amount of photos of persons

## Create and train model

All the steps are described in a [jupyter notebook, please see here for details](https://github.com/TobiasSunderdiek/cartoon-gan/blob/master/CartoonGAN.ipynb).

## References

\[1\] http://openaccess.thecvf.com/content_cvpr_2018/papers/Chen_CartoonGAN_Generative_Adversarial_CVPR_2018_paper.pdf

\[2\] https://www.kaggle.com/alamson/safebooru

\[3\] http://cocodataset.org

\[4\] https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocoDemo.ipynb

\[5\] http://images.cocodataset.org/annotations/annotations_trainval2017.zip
