PIL/Pillow GGB Tutorial
=======================

Introduction
------------

PIL/Pillow has a different scheme in gathering pixel value. It utilizes ``Image`` class to perform some image processing methods. This following tutorial will use PIL/Pillow as the main image processing library.

Load Image
----------

First of all, load the useful components to load an image::

    from PIL import Image
    from ggb import GGB, ColorSpace, CVLib
    
    image = Image.open('/path/to/image').convert('RGB')

.. warning:: Users should define ``/path/to/image`` to a valid path by themselves for example ``img/leukocytes.png``.

GGB Convert 
-----------

For the main process, let's utilize ``GGB``, ``ColorSpace`` and ``CVLib``::

    ggb_image = GGB(image=image, input_color=ColorSpace.RGB, backend=CVLib.PIL).process()

.. note:: Default PIL image in RGB color space. To see the valid color space please see the reference.

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
