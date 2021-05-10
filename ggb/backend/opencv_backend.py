import cv2
import numpy as np

from ggb.utils.constant import ColorSpace


def preprocessing(image, input_color=ColorSpace.RGB):
    """Preprocess source image. 
    
    :param image: source image
    :param input_color: source image color space
    :return:
    """
    img = image
    if input_color == ColorSpace.BGR:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif input_color == ColorSpace.HSV:
        img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_YUV2RGB)
    return img


def split_normalize(image):
    """Splitting source image then normalize it.
    
    :param image: source image
    :return: blue and green channel
    """
    _, g_, b_ = cv2.split(image)
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
    return b_, g_


def postprocessing(b, g, **kwargs):
    """Final GGB process.
    
    :param b: blue channel
    :param g: green channel
    :param kwargs: dict of custom variable
    :return: GGB image
    """
    inverse = False
    if 'inverse' in kwargs:
        inverse = kwargs['inverse']
    img = cv2.merge((b,g,g)) if not inverse else cv2.merge((g,g,b))
    return img
