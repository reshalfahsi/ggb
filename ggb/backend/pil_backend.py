import cv2
import numpy as np

import PIL
from PIL import Image, ImageOps
from PIL.ImageStat import Stat

from ggb.utils.constant import ColorSpace


def preprocessing(image, input_color=ColorSpace.RGB):
    """Preprocess source image. 
    
    :param image: source image
    :param input_color: source image color space
    :return:
    """
    img = image
    if input_color == ColorSpace.BGR:
        img = np.array(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
    elif input_color == ColorSpace.HSV:
        img = np.array(img)
        img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
        img = Image.fromarray(img)
    else:
        img = np.array(img)
        img = cv2.cvtColor(img, cv2.COLOR_YUV2RGB)
        img = Image.fromarray(img)
    return img


def split_normalize(image):
    """Splitting source image then normalize it.
    
    :param image: source image
    :return: blue and green channel
    """
    im = Image.Image.split(image)
    g = ImageOps.equalize(im[1], mask = None)
    mean = Stat(im[2]).mean[0]
    b = np.array(im[2]).astype('float32')
    b /= (1.0 + mean) 
    mean = Stat(g).mean[0]
    g = np.array(g).astype('float32')
    g /= (1.0 + mean)
    b = np.clip(b, 0, 1)
    g = np.clip(g, 0, 1)
    b *= 255.0
    g *= 255.0
    b = Image.fromarray(b.astype('uint8'))
    g = Image.fromarray(g.astype('uint8'))
    return b, g


def postprocessing(b, g, **kwargs):
    """Final GGB process.
    
    :param b: blue channel
    :param g: green channel
    :param kwargs: dict of custom variable
    :return: GGB image
    """
    img = Image.merge('RGB', (g, g, b))
    return img
