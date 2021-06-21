from __future__ import absolute_import

from ggb.utils.image import GGBImage
from ggb.utils import ColorSpace, CVLib
from ggb.utils import ColorSpaceError, ComputerVisionLibraryError
import ggb.backend as B

import numpy as np


class GGB(GGBImage):
    """GGB color space converter.

    :param image: image source either from path or variable
    :param input_color: color space of source image
    :param backend: computer vision library which handle the task
    """
    def __init__(self, image=None, input_color=ColorSpace.RGB, backend=CVLib.OPENCV):
        try:
            assert(isinstance(input_color, ColorSpace))
            self._img_color_space = input_color
        except:
            raise ColorSpaceError(input_color)
        try:
            assert(isinstance(backend, CVLib))
            super(GGB, self).__init__(image, backend)
        except:
            raise ComputerVisionLibraryError(backend)

    def process(self, **kwargs):
        """Main process of GGB.

        :param kwargs: dict of custom variable
        :return: GGBImage instance
        """
        allowed_kwargs = {'inverse'}
        for k in kwargs:
            if k not in allowed_kwargs:
                raise TypeError('Unexpected keyword argument '
                                'passed to GGB: ' + str(k))
        img = B.process(self.write(), self._img_color_space, self.backend(), **kwargs)
        return GGBImage(img, self.backend(), **kwargs)
