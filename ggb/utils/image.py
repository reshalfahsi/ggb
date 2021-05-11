from ggb.utils.constant import ColorSpace, CVLib
from ggb.utils.error import ColorSpaceError

import numpy as np

class GGBImage(object):
    """Image handler for GGB.
    
    :param image: image source either from path or variable
    :param backend: computer vision library which handle the task
    """
    def __init__(self, image=None, backend=CVLib.OPENCV):
        self.__backend = backend
        self.__image = self.__read(image, backend)


    def backend(self):
        """Check which computer vision library is used as backend
        
        :return: type of computer vision library
        """
        return self.__backend


    def __read(self, source, backend=CVLib.OPENCV):
        """Read image from source.
    
        :param source: image source either from path or variable
        :param backend: computer vision library which handle the task
        :return: image variable
        """
        if isinstance(source, str):
            if backend == CVLib.OPENCV:
                self.__backend = CVLib.OPENCV
                import cv2
                return cv2.imread(path)
            else:
                self.__backend = CVLib.PIL
                from PIL import Image
                return Image.open(path).convert('RGB')
        else:
            if isinstance(source, np.ndarray):
                self.__backend = CVLib.OPENCV
            else:
                self.__backend = CVLib.PIL
            return source


    def write(self, path=None, **kwargs):
        """Write the image into a file when path is not None 
           or variable when path is None.
         
        :param path: path to file
        :param kwargs: dict of custom variable
        """
        allowed_kwargs = {'inverse'}
        for k in kwargs:
            if k not in allowed_kwargs:
                raise TypeError('Unexpected keyword argument '
                                'passed to GGBImage: ' + str(k))
        if path == None:
            if self.__backend == CVLib.OPENCV:
                image = self.__image.astype('uint8')
                return image
            return self.__image
        else:
            if self.__backend == CVLib.OPENCV:
                import cv2
                image = self.__image.astype('uint8')
                if 'inverse' in kwargs:
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) if kwargs['inverse'] else image
                cv2.imwrite(path, image)
            else:
                self.__image.save(path)


    def show(self, **kwargs):
        """Show the image.

        :param kwargs: dict of custom variable
        """
        allowed_kwargs = {'inverse'}
        for k in kwargs:
            if k not in allowed_kwargs:
                raise TypeError('Unexpected keyword argument '
                                'passed to GGBImage: ' + str(k))
        if self.__backend == CVLib.OPENCV:
            import cv2
            image = self.__image.astype('uint8')
            if 'inverse' in kwargs:
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) if kwargs['inverse'] else image
            cv2.imshow("GGB", image)
            cv2.waitKey(0)
        else:
            self.__image.show()
