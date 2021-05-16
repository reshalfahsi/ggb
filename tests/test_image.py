import pytest
import cv2
import random
import numpy as np
from PIL import ImageChops

from ggb import GGB, CVLib, ColorSpace
from ggb.testing import ggb_test
from ggb.testing import get_image_from_url, get_random_image


@ggb_test
def test_opencv_difference():
    reference_image = get_image_from_url('https://github.com/reshalfahsi/GGB/raw/master/docs/img/leukocytes_ggb.png')
    image = get_image_from_url('https://github.com/reshalfahsi/GGB/raw/master/docs/img/leukocytes.png')
    ggb_image = GGB(image=image, input_color=ColorSpace.BGR).process()
    np.testing.assert_array_equal(ggb_image.write(), reference_image)


@ggb_test
def test_pil_difference():
    reference_image = get_image_from_url('https://github.com/reshalfahsi/GGB/raw/master/docs/img/leukocytes_ggb_pil.png', CVLib.PIL)
    image = get_image_from_url('https://github.com/reshalfahsi/GGB/raw/master/docs/img/leukocytes.png', CVLib.PIL)
    ggb_image = GGB(image=image, input_color=ColorSpace.RGB).process()
    assert(not ImageChops.difference(ggb_image.write(), reference_image))


@ggb_test
def test_opencv_channel():
    w = random.randint(16, 2048)
    h = random.randint(16, 2048)
    c = random.randint(1, 16)
    c = random.randint(8, 16) if ((c == 3) or (c==4)) else c
    image = get_random_image(w, h, c, CVLib.OPENCV)
    flag = None

    try:
        ggb_image = GGB(image=image).process()
        flag = False
    except:
        flag = True
    assert(flag)


@ggb_test
def test_pil_channel():
    w = random.randint(16, 2048)
    h = random.randint(16, 2048)
    c = random.randint(1, 16)
    c = random.randint(8, 16) if ((c == 3) or (c==4)) else c
    flag = None

    try:
        image = get_random_image(w, h, c, CVLib.PIL)
        ggb_image = GGB(image=image).process()
        flag = False
    except:
        flag = True
    assert(flag)


@ggb_test
def test_color_space():
    reference_image = get_image_from_url('https://github.com/reshalfahsi/GGB/raw/master/docs/img/leukocytes_ggb.png')
    image = get_image_from_url('https://github.com/reshalfahsi/GGB/raw/master/docs/img/leukocytes.png')
    ggb_image = GGB(image=image, input_color=ColorSpace.BGR, backend=CVLib.OPENCV).process()
    np.testing.assert_array_equal(ggb_image.write(), reference_image)

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    ggb_image = GGB(image=rgb_image, input_color=ColorSpace.RGB, backend=CVLib.OPENCV).process()
    np.testing.assert_array_equal(ggb_image.write(), reference_image)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    ggb_image = GGB(image=hsv_image, input_color=ColorSpace.HSV, backend=CVLib.OPENCV).process()
    np.testing.assert_array_equal(ggb_image.write(), reference_image)

    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    ggb_image = GGB(image=yuv_image, input_color=ColorSpace.YUV, backend=CVLib.OPENCV).process()
    np.testing.assert_array_equal(ggb_image.write(), reference_image)


if __name__ == '__main__':
    pytest.main([__file__])
