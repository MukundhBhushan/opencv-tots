# opencv-tots

## Thresholding
Segmentation technique used to seperate object from its background. 
Each pixel of an image is compared with a predefined threshold value

Syntax:- 
```python
_, varname = cv.threshold("<image file>",<thrshold value>,<maximum value>,<threshold techniques>)
```

Thresholding techniques in opencv:
* THRESH_BINARY
Converts the image into 2 color representation. Pixel values greater than the threshold are white. Lesser than the threshold are black

* THRESH_BINARY_INV
Inverse of the THRESH_BINARY

* THRESH_TRUNC
pixel values lesser that or equal to the thershold value will not change. Values above the treshold are assigned the treshold value itself 

* THRESH_TOZERO
values lower than the treshold are assigned 0. Above the treshold will remain same. 

*THRESH_TOZERO_INV
Inverse of THRESH_TOZERO greater than treshold is 0. Lesser than threshold remoain the same

## Adaptive threshold
Syntax
```python
varname = cv2.adaptiveThreshold("<image file>",<adaptive technique>, <thresholding technique>,<blocksize>,<C value>)
```
<adaptive technique>: ADAPTIVE_THRESH_MEAN_C, ADAPTIVE_THRESH_GAUSSIAN_C
<thresholding technique>: THRESH_BINARY, THRESH_BINARY_INV, THRESH_TRUNC, THRESH_TOZERO, THRESH_TOZERO_INV
<blocksize>: regoin size
<C value>: constant value which is used to subtract from the mean or the weighted sum


Thresholds are calculated for smaller regions instead of having an global threshold value for the entire picture. These threshold values change from region to region

Adaptive thresholding techniques in opencv:  
* ADAPTIVE_THRESH_MEAN_C
Threshold value is determined by the mean of a region ie blocksize X blocksize X blocksize minus C

* ADAPTIVE_THRESH_GAUSSIAN_C
Is the weighted sum ie sum of( wight X pixel value) of a blocksize X blocksize region minus C


## Morphological techniques
Normally performed on binary images

Requires:- 
* Original image
* Kernal: matrix of fixed dimesions. Helps in deciding the nature of operation.
* mask: Converting the image to greyscale and thresholding 

Techiques:- 
* Dilation 
```python
dilation = cv2.dilate(mask, kernal, iterations=2)
``` 
    * Dilation helps in removing noise from image 
    * Increase the white area of the image (as image is binary)
    * itteration is how many times u want to execute the dilation step 
    * bigger the kernal better the dilation optimal (5,5) but detected boundary size increases more than it actually is
    * causes overlap if the white areas are too close if the itterationa are high

* Erosion
```python
erosion = cv2.erode(mask, kernal, iterations=1)
```
    * Helps in reducing the baindary size of the foreground object
    * Increases the size of the black around the object's boundary
    * The kernal slides over the image and the value 1 is assigned only if all the values under the kernal is 1 else 0.
     
* MorphologyEx
    * opening
        ```python
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
        ```
        * Erosion -> Dilation 

    * opening
        ```python
        closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
        ```
        * Dilation -> Erosion 

    * Morphological gradeint
        ```python
        mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
        ```
        * pixel difference between dilation and errosion

    * Morphological Tophat
        ```python
        th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)
        ```
        * Pixel difference between actual image and MORPH_OPEN


## Filters
Blurs out the corners ie smoothens the image.
Removes noise in  the image
* Homogeneous Filters
    Syntax
    ```python
    dst = cv2.filter2D(<image file>, <depth>, <kernel size>)
    ```
    Easiest filters. The mean off the values under the kernal matrix
    Each pixel value have equal weights
    formula = (1/k_width X k_height)[blocksize X blocksize 1's]

* Blur
    Syntax
    ```python
    blur = cv2.blur(<image file>, kernal)
    ```
    Averaging based algorithm

* Gaussian filters
```python
gblur = cv2.GaussianBlur(<img file>, <kernal>, <Sigmax vlaue>)

```
    !()[https://i.stack.imgur.com/Qc4Mq.gif]
    The weights are not equal.
    The weights in the middel are heigher than the weights around 
    

* MedianBlur
    ```python
    median = cv2.medianBlur(img, 5)
    ```

    This filter needs an odd numbered kernal size
    This filter is best for salt and pepper noise

## Salt and pepper noise
Noise where in some places white noise and other places black noise
!(salt)[https://www.fit.vutbr.cz/~vasicek/imagedb/img_corrupted/impnoise_005/106020.png]

## Image gradients

* Laplacian
    ```python
    lap = cv2.Laplacian(img, cv2.CV_64F, ksize=<kernal size>) 
    lap = np.uint8(np.absolute(lap))
    ```
    cv2.CV_64: is a datatype which allows for -ve values as well
    uint8 converts the image back to the unsigned int
    Ksize: lower the value more pronounced the boundary lines


* Soble
Syntax
```python
    sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0,ksize=kernal size)
    sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1,ksize=kernal size)
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))
```

x axis = (1,0)
y axis = (0,1)

The values most be converted back to unsigned int
