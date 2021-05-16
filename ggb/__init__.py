"""

This package is implementation of GGB color space from
Development of a Robust Algorithm for Detection of Nuclei and Classification of White Blood Cells in Peripheral Blood Smear Images.

https://link.springer.com/content/pdf/10.1007%2Fs10916-018-0962-1.pdf


"""

from __future__ import absolute_import

from ggb.ggb import GGB
from ggb.utils import ColorSpace, CVLib
import ggb.testing as testing
import ggb.backend as backend

__version__ = '1.1.2'
