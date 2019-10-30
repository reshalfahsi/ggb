## This script is implementation of GGB color space from Development of a Robust Algorithm for Detection of Nuclei and Classification of White Blood Cells in Peripheral Blood Smear Images, https://link.springer.com/content/pdf/10.1007%2Fs10916-018-0962-1.pdf ##

import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse
import bisect
import math

def imadjust(src, vin=[0,255], vout=(0,255), tol=0.001):
    # src : input one-layer image (numpy array)
    # tol : tolerance, from 0 to 100.
    # vin  : src image bounds
    # vout : dst image bounds
    # return : output img

    dst = src.copy()
    tol = max(0, min(100, tol))

    if tol > 0:
        # Compute in and out limits
        # Histogram
        hist = np.zeros(256, dtype=np.int)
        for r in range(src.shape[0]):
            for c in range(src.shape[1]):
                hist[src[r,c]] += 1
        # Cumulative histogram
        cum = hist.copy()
        for i in range(1, len(hist)):
            cum[i] = cum[i - 1] + hist[i]

        # Compute bounds
        total = src.shape[0] * src.shape[1]
        low_bound = total * tol / 100
        upp_bound = total * (100 - tol) / 100
        vin[0] = bisect.bisect_left(cum, low_bound)
        #print vin[0]
        vin[1] = bisect.bisect_left(cum, upp_bound)
        #print vin[1]

    # Stretching
    scale = (vout[1] - vout[0]) / (vin[1] - vin[0])
    for r in range(dst.shape[0]):
        for c in range(dst.shape[1]):
            vs = max(src[r,c] - vin[0], 0)
            vd = min(int(vs * scale + 0.5) + vout[0], vout[1])
            dst[r,c] = vd
    return dst

def max_min(src):
    row = src.shape[0]
    col = src.shape[1]
    pmin = 255
    pmax = 0
    for r in range(0,row):
        for c in range(0, col):
            pmin = min(pmin, src[r,c])
            pmax = max(pmax, src[r,c])
    print pmax
    print pmin
    return pmax, pmin

def ggb():
    global parser
    args = parser.parse_args()
    bgr = cv2.imread(args.input)
    b,g,r = cv2.split(bgr)
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    pmax, pmin = max_min(g)
    _g = imadjust(g, vin=[pmin, pmax])
    ggb = cv2.merge((_g,_g,b))
    plt.subplot(1,2,1)
    plt.imshow(ggb)
    plt.title("GGB")
    plt.xticks([])
    plt.yticks([])
    plt.subplot(1,2,2)
    plt.imshow(rgb)
    plt.title("RGB")
    plt.xticks([])
    plt.yticks([])
    plt.savefig('GGB_RGB.jpg')
    plt.clf()

if __name__ == '__main__':
    global parser   
    parser = argparse.ArgumentParser(description='Code for Changing RGB Image to GGB Image')
    parser.add_argument('--input', help='Path to input image', default='leukocytes.png')
    ggb()
