from ggb.utils.constant import ColorSpace, CVLib
from ggb.utils.error import ComputerVisionLibraryError

import numpy as np


class GGBImage(object):
    """Image handler for GGB.

    :param image: image source either from path or variable
    :param backend: computer vision library which handle the task
    :param kwargs: dict of custom variable
    """
    def __init__(self, image=None, backend=CVLib.OPENCV, **kwargs):
        allowed_kwargs = {'inverse'}
        for k in kwargs:
            if k not in allowed_kwargs:
                raise TypeError('Unexpected keyword argument '
                                'passed to GGBImage: ' + str(k))
        assert(isinstance(backend, CVLib))
        self.__inverse = False
        if 'inverse' in kwargs:
            self.__inverse = True if kwargs['inverse'] else False
        self.__backend = backend
        self.__image = self.__read(image)

    def backend(self):
        """Check which computer vision library is used as backend.

        :return: type of computer vision library
        """
        return self.__backend

    def __read(self, source):
        """Read image from source.

        :param source: image source either from path or variable
        :return: image variable
        """
        if isinstance(source, str):
            if self.__backend == CVLib.OPENCV:
                import cv2
                return cv2.imread(path)
            else:
                from PIL import Image
                return Image.open(path).convert('RGB')
        else:
            if isinstance(source, np.ndarray):
                self.__backend = CVLib.OPENCV
                assert((source.ndim == 3) and ((source.shape[-1] == 3) or (source.shape[-1] == 4)))
            else:
                try:
                    source = source.convert('RGB')
                    self.__backend = CVLib.PIL
                except:
                    raise ComputerVisionLibraryError
            return source

    def write(self, path=None):
        """Write the image into a file when path is not None or variable when path is None.

        :param path: path to file
        """
        if path is None:
            if self.__backend == CVLib.OPENCV:
                image = self.__image.astype('uint8')
                return image
            return self.__image
        else:
            if self.__backend == CVLib.OPENCV:
                import cv2
                image = self.__image.astype('uint8')
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) if self.__inverse else image
                cv2.imwrite(path, image)
            else:
                self.__image.save(path)

    def show(self):
        """Show the image.
        """
        if self.__backend == CVLib.OPENCV:
            import cv2
            image = self.__image.astype('uint8')
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) if self.__inverse else image
            cv2.imshow("GGB", image)
            cv2.waitKey(0)
        else:
            self.__image.show()
