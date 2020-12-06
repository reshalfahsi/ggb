## This script is implementation of GGB color space from Development of a Robust Algorithm for Detection of Nuclei and Classification of White Blood Cells in Peripheral Blood Smear Images, https://link.springer.com/content/pdf/10.1007%2Fs10916-018-0962-1.pdf ##

import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse
import math

def ggb():
    global parser
    args = parser.parse_args()
    bgr = cv2.imread(args.input)
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    b_, g_, _ = cv2.split(bgr)
    g_ = cv2.equalizeHist(g_)
    b_ = b_.astype('float32')
    g_ = g_.astype('float32')
    mean = np.mean(b_)
    b_ /= (mean + 1.0)
    mean = np.mean(g_)
    g_ /= (mean + 1.0)
    b_ = np.clip(b_, 0, 1)
    g_ = np.clip(g_, 0, 1)
    b_ *= 255.0
    g_ *= 255.0
    ggb = cv2.merge((b_,g_,g_))
    cv2.imwrite("GGB.jpg",ggb)
    ggb = cv2.merge((g_,g_,b_))
    plt.subplot(1,2,1)
    plt.imshow(ggb.astype('uint8'))
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
    parser.add_argument('--input', help='Path to input image', default='img/leukocytes.png')
    ggb()
