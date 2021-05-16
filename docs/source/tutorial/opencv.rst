OpenCV GGB Tutorial
===================

Introduction
------------

OpenCV uses ``numpy`` based array format to store the pixel value of an image. 
Thus, the ``numpy`` array is heavily used as core of GGB color space converter which OpenCV as its backend.
This following tutorial will use OpenCV as the main image processing library.

Load Image
----------

First of all, load the useful components to load an image::

    import cv2
    from ggb import GGB, ColorSpace, CVLib
    
    image = cv2.imread('/path/to/image')

.. warning:: Users should define ``/path/to/image`` to a valid path by themselves for example ``img/leukocytes.png``.

GGB Convert 
-----------

For the main process, let's utilize ``GGB``, ``ColorSpace`` and ``CVLib``::

    ggb_image = GGB(image=image, input_color=ColorSpace.BGR, backend=CVLib.OPENCV).process()

.. note:: Default OpenCV image in BGR color space. To see the valid color space please see the reference.

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
