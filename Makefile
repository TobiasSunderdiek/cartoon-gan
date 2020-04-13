install:
	pip install -r requirements.txt

cartoons:
	python cartoon_image_downloader.py

cartoons-smooth:
	python cartoon_image_smoothing.py

photos:
	python photo_downloader.py

install-transform:
	pip install -r requirements-transform.txt

transform:
	python transform.py $(IMAGE)
