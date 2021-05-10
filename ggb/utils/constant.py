from enum import Enum


class ColorSpace(Enum):
    """Valid color spaces.
    """
    RGB = 1
    BGR = 2
    HSV = 3
    YUV = 4


class CVLib(Enum):
    """Supported computer vision libraries.
    """
    OPENCV = 1
    PIL = 2
