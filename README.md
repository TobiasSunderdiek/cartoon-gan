# CartoonGAN - my attempt to implement it

Within this repo, I try to implement a cartoon GAN \[Chen et al., CVPR18\].

I created a github page for detailed documentation, please see https://tobiassunderdiek.github.io/cartoon-gan/ for details.

![result.png](https://raw.githubusercontent.com/TobiasSunderdiek/cartoon-gan/gh-pages/assets/result.png "result example")

## Usage

### Step 1: Generate datasets

All scripts to create the images are resumeable. It is possible to run `make cartoons` and `make photos` in parallel by calling them manually in separate terminals.

#### Cartoon images

- download `all_data.csv` from safebooru dataset \[2\]
- point to `all_data.csv` in `PATH_TO_SAFEBOORU_ALL_DATA_CSV` of `cartoon_image_downloader.py`
- run `make install` to install necessary libraries
- run `make cartoons` to download configurable amount of medium size images

#### Edge-smoothed version of cartoon images

- run `make cartoons-smooth` to create the images

#### Photos

- download and unzip coco annotations from \[3\]
- configure annotations dir location in `PATH_TO_COCO_ANNOTATIONS_ROOT_FOLDER` of `photo_downloader.py`
- run `make photos` to download configurable amount of photos of persons

### Step 2: Train model

All the steps are described in a [jupyter notebook on colab, please see here for details.](https://github.com/TobiasSunderdiek/cartoon-gan/blob/master/CartoonGAN.ipynb)

### Step 3: Test

- run `make install-transform`
- download pre-trained weights, they are available for download as part of [the release here.](https://github.com/TobiasSunderdiek/cartoon-gan/releases).
- run `make transform IMAGE=some_example_image_path`

Additional information about how to load the pre-trained weights and transform images can be found in the project documentation here: https://tobiassunderdiek.github.io/cartoon-gan/ .

### Credits

Thanks to the authors \[Chen et al., CVPR18\] of the paper for their great work.

## References

\[Chen et al., CVPR18\] http://openaccess.thecvf.com/content_cvpr_2018/papers/Chen_CartoonGAN_Generative_Adversarial_CVPR_2018_paper.pdf

\[2\] https://www.kaggle.com/alamson/safebooru/download

\[3\] http://images.cocodataset.org/annotations/annotations_trainval2017.zip
