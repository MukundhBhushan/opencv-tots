#Morphological transformations are operations done on the image shape 
#performed on a binary image
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5,5), np.uint8) #same as (5,5) inplace of the variable "kernal"

dilation = cv2.dilate(mask, kernal, iterations=2) #dilation helps in removing noise from image
#itteration is how many times u want to execute the dilation step
#bigger the kernal better the dilation optimal (5,5)
#but detected boundary size increases more than it actually is
erosion = cv2.erode(mask, kernal, iterations=1) #reduces the size of detected object.
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal) #erosion followed by dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal) #dilation followed by errosion 
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)#difference between dilation and errosion
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)#difference between actual image and MORPH_OPEN

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()