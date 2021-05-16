"""

Computer vision library backend for converting to GGB Image.

"""

from ggb.utils import CVLib

def process(image, color_space, backend, **kwargs):
    """The main proces of GGB converter.

    :param image: input image
    :param color_space: input image color space
    :param backend: computer vision library backend
    :param kwargs: custom dict parameter
    :return: image in GGB color space
    """
    if backend == CVLib.OPENCV:
        from ggb.backend.opencv_backend import preprocessing, split_normalize, postprocessing
    else:
        from ggb.backend.pil_backend import preprocessing, split_normalize, postprocessing

    img = preprocessing(image, color_space)
    b, g = split_normalize(img)
    img = postprocessing(b, g, **kwargs)
    return img
