# Blur Detection in Lower Jaw Images

In this project laplacian filter is applied on each image and the variance of the image is gotten after being filtered. A threshold on variance is defined to determine whether the image is blurry or not.

## Laplacian Filter
The Laplacian is a 2-D isotropic measure of the 2nd spatial derivative of an image. The Laplacian of an image highlights regions of rapid intensity change and is therefore often used for edge detection. The operator normally takes a single graylevel image as input and produces another graylevel image as output. 

After applying the laplacian filter, the assumption here is that if an image contains high variance then there is a wide spread of responses, both edge-like and non-edge like, representative of a normal, in-focus image. But if there is very low variance, then there is a tiny spread of responses, indicating there are very little edges in the image. As we know, the more an image is blurred, the less edges there are.

## Threshold

Setting the correct threshold is quite domain dependent. Too low of a threshold and you’ll incorrectly mark images as blurry when they are not. Too high of a threshold then images that are actually blurry will not be marked as blurry.


In this project, for defining the best threshold, numerous images with different bluriness degrees was constructed and tested.
Consequently, a hard and a soft threshold are defined for various purposes.

## Setup
For installing requirements, run the following on terminal:
```
pip install -r requirements.txt
```
For running the project use the following:
```
python3 blur_detection.py your_image_path your_threshold_type
```