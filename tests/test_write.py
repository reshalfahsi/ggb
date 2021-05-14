import cv2
from PIL import Image
import numpy as np
import random
import pytest

from ggb import GGB, GGBImage
from ggb.utils.test import ggb_test
from ggb.utils.test import get_random_image, get_filled_image


@ggb_test
def test_opencv_write():
    w = random.randint(16, 2048)
    h = random.randint(16, 2048)
    image = get_random_image(w, h, 3, CVLib.OPENCV)

    ggb_image = GGB(image=image).process()
    assert(isinstance(ggb_image.write(), np.ndarray) is True)

    w = random.randint(16, 2048)
    h = random.randint(16, 2048)
    value = random.randint(0, 255)
    image = get_filled_image(w, h, 3, value, CVLib.OPENCV)

    ggb_image = GGB(image=image).process()
    assert(isinstance(ggb_image.write(), np.ndarray) is True)


@ggb_test
def test_pil_write():
    w = random.randint(16, 2048)
    h = random.randint(16, 2048)
    image = get_random_image(w, h, 3, CVLib.PIL)

    ggb_image = GGB(image=image).process()
    assert(isinstance(ggb_image.write(), np.ndarray) is False)

    w = random.randint(16, 2048)
    h = random.randint(16, 2048)
    value = random.randint(0, 255)
    image = get_filled_image(w, h, 3, value, CVLib.PIL)

    ggb_image = GGB(image=image).process()
    assert(isinstance(ggb_image.write(), np.ndarray) is False)


if __name__ == '__main__':
    pytest.main([__file__])
