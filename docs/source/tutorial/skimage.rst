``scikit-image`` GGB Tutorial
=============================

Introduction
------------

``scikit-image`` or skimage as same as OpenCV uses 
``numpy`` array as its core for image processing. 
Thus, this tutorial is similar to the OpenCV ones with a slightly different configuration. This following tutorial will use ``scikit-image`` as the main image processing library.

Load Image
----------

First of all, load the useful components to load an image::

    from skimage import io
    from ggb import GGB, ColorSpace, CVLib
    
    image = io.imread('/path/to/image')

.. warning:: Users should define ``/path/to/image`` to a valid path by themselves for example ``img/leukocytes.png``.

GGB Convert 
-----------

For the main process, let's utilize ``GGB``, ``ColorSpace`` and ``CVLib``::

    ggb_image = GGB(image=image, input_color=ColorSpace.RGB, backend=CVLib.OPENCV).process()

.. note:: Default ``scikit-image`` image in RGB color space. To see the valid color space please see the reference.

.. warning:: ``scikit-image`` backend parameter should be set as ``CVLib.OPENCV`` since it is based on ``numpy`` array.

Show Result
-----------

There are various ways to see the result such as show it directly or write it into a variable or file::

    #show it directly
    ggb_image.show()

    #write it into a variable
    final_image = ggb_image.write()

    #write it into a file
    ggb_write.write('/path/to/image')

.. warning:: Users should define ``/path/to/image`` to a valid path by themselves for example ``img/leukocytes_ggb.png``.
