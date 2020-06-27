# cv2_plt_imshow
Using matplotlib_imshow for images read by cv2 

## Introduction
One of the major issue faced while using `cv2`, especially when you are using `jupyter-notebooks`, is to perform `cv2.imshow` the kernel breaks. Apart from this, most of the users are comfortable using matplotlib for display, specially its display in notebook using `%matplotlib inline` magic. 

This package provides two of the main function, converting the image to a format more suitable in matplotlib, and plotting the image using matplotlib in the notebooks.

## Table of contents
* [Setup](#setup)
* [Usage](#usage)
* [Dependencies](#dependencies)
* [Contact](#contact)

## Setup
```pip install cv2_plt_imshow```

## Usage

```
import cv2
import matplotlib.pyplot as plt
from cv2_plt_imshow import cv2_plt_imshow, plt_format

# read image
im1 = cv2.imread('./images/potrait.jpg')

# use cv2_plt_imshow function to plot any image that was read by cv2, but is plotted using pyplot
cv2_plt_imshow(im1)

# Convert the image to be suitable for pyplot format and later use it for plotting using pyplot functions
im2 = cv2.imread('./images/landscape.jpg')
fig, axs = plt.subplots(2 , figsize=(20,20))
fig.suptitle('Vertically stacked subplots')
axs[0].imshow(plt_format(im1))
axs[1].imshow(plt_format(im2))
```

## Dependencies
* [matplotlib](https://pypi.org/project/matplotlib/)
* [cv2](https://pypi.org/project/opencv-python/)

## Contact
* [Author](https://rupesh.info/)
* [Github](https://github.com/rs9899/cv2_plt_imshow)
