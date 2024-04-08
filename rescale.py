import cv2 as cv
"""Image DownScaling Functions"""
def rescaleFrame(frame,scale =0.75):
   # img vids and live vid
    width  = int(frame.shape[1]*scale)
    height  = int(frame.shape[0]*scale)

    dimensions = width,height
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

"""Changing vid resolution using img.set()"""
def changeRes(capture,width,heigh):
    # only img
    capture.set(3,width)
    capture.set(4,heigh)
    return capture
