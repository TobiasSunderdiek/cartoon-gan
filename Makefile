install:
	pip install -r requirements.txt

cartoons:
	python cartoon_image_downloader.py

cartoons-smooth:
	python cartoon_image_smoothing.py

photos:
	python photo_downloader.py

transform:
	python transform.py $(IMAGE)
