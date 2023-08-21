import cv2 as cv
import numpy as np
import os
import win32api, win32con
from time import time
from windowcapture import WindowCapture
from vision import Vision

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture()
# initialize the Vision class
head = Vision('head.jpg')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    points = head.find(screenshot, 0.5, 'rectangles')
    if(points):
        print('Move Mouse...')
        win32api.SetCursorPos((points[0],points[1]))
        cv.waitKey()
    else:
        print('No Head found')
print('Done.')
