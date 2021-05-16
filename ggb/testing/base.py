import six
import cv2
import numpy as np
import cv2
from PIL import Image

try:
    import urllib.request as urllib
except:
    import urllib

from ggb.utils.constant import CVLib, ColorSpace
from ggb.utils.error import ComputerVisionLibraryError


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
        try:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image).convert('RGB')
        except:
            raise ComputerVisionLibraryError
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
        try:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image).convert('RGB')
        except:
            raise ComputerVisionLibraryError
    return image


def get_image_from_url(url, backend=CVLib.OPENCV):
    """Obtain an image from URL.

    :param url: url to the image
    :param backend: computer vision library image output format
    :return: downloaded image
    """
    req = urllib.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    if backend == CVLib.PIL:
        try:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image).convert('RGB')
        except:
            raise ComputerVisionLibraryError
    return img


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
