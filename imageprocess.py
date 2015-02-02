# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 15:13:22 2015

@author: zwl
"""
import matplotlib.image as image
import matplotlib.pyplot as plt
imarray=image.imread("./default_head.png")
plt.imshow(imarray)

red,yellow=imarray.copy(),imarray.copy()
red[:,:,(1,2)]=0
yellow[:,:,2]=0
plt.imshow(red)
plt.imshow(yellow)

from skimage.color import rgb2gray
gray_image=rgb2gray(imarray)
plt.imshow(gray_image)
print("imarray shape:",imarray.shape)
print("gray_image shape:",gray_image.shape)

from skimage.filter import threshold_otsu
thresh=threshold_otsu(gray_image)
binary=gray_image>thresh
plt.imshow(binary)

from skimage.filter import gaussian_filter
blurred_image=gaussian_filter(gray_image,sigma=20)
plt.imshow(blurred_image)