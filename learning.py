#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 23:40:31 2018

@author: satya
"""

import cv2 as cv;
import numpy as np;

def main():
    imgpath = "/home/satya/opencv/standard_test_images/lena.tif";
    img = cv.imread(imgpath);
    cv.imshow("lena",img);
    cv.waitKey(0);
    cv.destroyWindow('lena');

if __name__ == "__main__":
    main();