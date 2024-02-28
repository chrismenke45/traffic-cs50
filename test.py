import os
import cv2
import numpy as np

IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
data_dir = "gtsrb"

current_working_directory = os.getcwd()

image_directory = os.path.join(current_working_directory, data_dir)

images = []
labels = []
# a = 0
for category_int in range(NUM_CATEGORIES):
    category_path = os.path.join(image_directory, str(category_int))
    if os.path.isdir(category_path):
        
        for filename in os.listdir(category_path):
            imagepath = os.path.join(category_path, filename)
            if os.path.isfile(imagepath):
                im = cv2.imread(imagepath, cv2.IMREAD_COLOR)
                resized_image = cv2.resize(im, (IMG_WIDTH, IMG_HEIGHT))
                resized_scaled_image = np.divide(resized_image, 255.0)
                images.append(resized_scaled_image)
                labels.append(category_int)
                # if a < 1:
                #     # print(type(resized_image))
                #     print(resized_image)
                #     scaled_image = np.divide(resized_image, 255.0)
                #     print(scaled_image)
                #     # print(type(category_int))
                #     # print(category_int)
                #     a += 1

# print(len(images))
# print(len(labels))
# current_working_directory = os.getcwd()

# image_directory = os.path.join(current_working_directory, "gtsrb")

# images = []
# labels = []

# for dirname in os.listdir(image_directory):
#     f = os.path.join(image_directory, dirname)
    
#     # checking if it is a directory with a integer for a name
#     if os.path.isdir(f):
#         a = 0
#         for filename in os.listdir(f):
#             imagepath = os.path.join(f, filename)
#             if os.path.isfile(imagepath):
#                 im = cv2.imread(imagepath, cv2.IMREAD_COLOR)
#                 resized_image = cv2.resize(im, (IMG_WIDTH, IMG_HEIGHT))
#                 images.append(resized_image)
#                 labels.append(dirname)


