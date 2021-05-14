import six
import cv2
import numpy as np
from PIL import Image

from ggb.utils.constant import CVLib, ColorSpace


def get_random_image(w, h, c=3, backend=CVLib.OPENCV):
    """Generates random image.

    :param w: image width
    :param h: image height
    :param c: image channel
    :param backend: computer vision library image output format
    :return: random image
    """
    image = np.random.randint(255, size=(w, h, c), dtype=np.uint8)
    if backend == CVLib.PIL:
        image = Image.fromarray(image)
    return image


def get_filled_image(w, h, c=3, value=0, backend=CVLib.OPENCV):
    """Generates same pixel value image.

    :param w: image width
    :param h: image height
    :param c: image channel
    :param value: same pixel value
    :param backend: computer vision library image output format
    :return: filled image
    """
    image = np.full((w, h, c), value, dtype=np.uint8)
    if backend == CVLib.PIL:
        image = Image.fromarray(image)
    return image


def ggb_test(func):
    """Wrapper to test function.

    :param func: test function
    :return: wrapper function
    """
    @six.wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret
    return wrapper
