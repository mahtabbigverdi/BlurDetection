import argparse
import os
import sys
import cv2

threshold_dict  = {'soft': 60, 'hard': 130 }


my_parser = argparse.ArgumentParser(description='Determine whether an image is blurry or not')

my_parser.add_argument('ImagePath',
                       metavar='Image Path',
                       type=str,
                       help='Path to the image for blur detection')

my_parser.add_argument('threshold_type',
                       metavar='Type of threshold',
                       type=str,
                       help='define the type of threshold, hard or soft')

args = my_parser.parse_args()

image_path = args.ImagePath
if not os.path.isfile(image_path):
    print('The path specified does not exist')
    sys.exit()

if args.threshold_type not in threshold_dict:
    print('The type of threshold is not defined')
    sys.exit()

threshold = threshold_dict[args.threshold_type]

# read image in grayscale mood for edge detection and further analysis
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

def get_variance(img):
    '''
    :param img: raw grayscale image
    :return: variance of image after applying laplacian filter
    '''
    # compute laplacian of the image to detect edges and sharp regions
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    return laplacian.var()

var_img = get_variance(img)

if var_img < threshold:
    print('Your image is blurry')
else:
    print('Your image is NOT blurry')
