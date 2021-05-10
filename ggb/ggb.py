from __future__ import absolute_import

from ggb.utils.image import GGBImage
from ggb.utils.constant import ColorSpace, CVLib
from ggb.utils.error import ColorSpaceError


import numpy as np


class GGB(GGBImage):
    """GGB color space converter.
    
    :param image: image source either from path or variable
    :param input_color: color space of source image 
    :param backend: computer vision library which handle the task
    """
    def __init__(self, image=None, input_color=ColorSpace.RGB, backend=CVLib.OPENCV):
        super(GGB, self).__init__(image, backend)
        try:
            assert(isinstance(input_color, ColorSpace))
            self.__img_color_space = input_color
        except:
            raise ColorSpaceError(input_color)


    def process(self, **kwargs):
        """Main process of GGB.
        
        :param kwargs: dict of custom variable
        """
        allowed_kwargs = {'inverse'}
        for k in kwargs:
            if k not in allowed_kwargs:
                raise TypeError('Unexpected keyword argument '
                                'passed to GGB: ' + str(k))
        if self.backend() == CVLib.OPENCV:
            from ggb.backend.opencv_backend import preprocessing, split_normalize, postprocessing
        else:
            from ggb.backend.pil_backend import preprocessing, split_normalize, postprocessing
        img = preprocessing(self.write(), self.__img_color_space)
        b, g = split_normalize(img)
        img = postprocessing(b, g, **kwargs)

        return GGBImage(img, self.backend())
