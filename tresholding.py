import cv2 as cv
import numpy as np

img = cv.imread('<image path>',0)
#format:
#   cv.threshold(img, <treshold>, <colur>, <technique>)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY) #if lower than treshold resultant pixel value is 0 ie black else white (255)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV) #opposite of THRESH_BINARY
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC) #upto the thershold pixel value will not change. Values above the treshold are assigned the treshold value itself 
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) #values lower than the treshold will be 0 above the treshold will remain same. 
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV) #opposite of THRESH_TOZERO greater than treshold is 0 


cv.imshow("Image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
cv.imshow("th4", th4)
cv.imshow("th5", th5)

cv.waitKey(0)
cv.destroyAllWindows()