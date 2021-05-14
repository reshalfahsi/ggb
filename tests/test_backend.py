import cv2
from PIL import Image
import random
import pytest

from ggb import GGB, GGBImage, CVLib
from ggb.utils.test import ggb_test
from ggb.utils.test import get_random_image, get_filled_image


@ggb_test
def test_opencv_backend():
    w = random.randint(16, 2048)
    h = random.randint(16, 2048)
    image = get_random_image(w, h, 3, CVLib.OPENCV)

    ggb_image = GGB(image=image).process()
    assert(ggb_image.backend() == CVLib.OPENCV)

    w = random.randint(16, 2048)
    h = random.randint(16, 2048)
    value = random.randint(0, 255)
    image = get_filled_image(w, h, 3, value, CVLib.OPENCV)

    ggb_image = GGB(image=image).process()
    assert(ggb_image.backend() == CVLib.OPENCV)



@ggb_test
def test_pil_backend():
    w = random.randint(16, 2048)
    h = random.randint(16, 2048)
    image = get_random_image(w, h, 3, CVLib.PIL)

    ggb_image = GGB(image=image).process()
    assert(ggb_image.backend() == CVLib.PIL)

    w = random.randint(16, 2048)
    h = random.randint(16, 2048)
    value = random.randint(0, 255)
    image = get_filled_image(w, h, 3, value, CVLib.PIL)

    ggb_image = GGB(image=image).process()
    assert(ggb_image.backend() == CVLib.PIL)


if __name__ == '__main__':
    pytest.main([__file__])
