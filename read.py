import cv2 as cv
import time
img1  = cv.imread('resources/Photos/cat.jpg')
img2  = cv.imread('resources/Photos/cat_large.jpg')

cv.imshow('Cat',img1)
cv.waitKey(0)

cv.imshow('Large Cat not visible',img2)

cv.waitKey(0)