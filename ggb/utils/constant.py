from enum import Enum


class ColorSpace(Enum):
    """Valid color spaces.
    """
    BGR = 1
    HSV = 2
    RGB = 3
    YUV = 4


class CVLib(Enum):
    """Supported computer vision libraries.
    """
    OPENCV = 1
    PIL = 2
