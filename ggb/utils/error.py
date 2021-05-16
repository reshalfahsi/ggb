from __future__ import absolute_import


class ColorSpaceError(Exception):
    """Exception raised for errors in the color space.


    :param color_space: color space which caused the error
    :param message: explanation of the error
    """
    def __init__(self, color_space, message="Color space is not supported"):
        self.color_space = color_space
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.color_space + ' -> ' + self.message


class ComputerVisionLibraryError(Exception):
    """Exception raised for errors in the computer vision library.


    :param cvlib: computer vision library which caused the error
    :param message: explanation of the error
    """
    def __init__(self, cvlib=None, message="Computer vision library is not supported"):
        self.cvlib = cvlib
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "Unknown computer vision library or invalid channel size" if self.cvlib is None else self.cvlib + ' -> ' + self.message
