from ggb import GGB, ColorSpace

import cv2
import urllib
import numpy as np

from PIL import Image

def main():
    # Load image from internet
    req = urllib.urlopen('https://github.com/reshalfahsi/GGB/raw/master/docs/img/leukocytes.png')
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    
    # Converting to GGB Color
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    ggb_image = GGB(image=img, input_color=ColorSpace.BGR).process()
    ggb_image.show()

    # Result
    img = ggb_img.write()    


if __name__ == '__main__':
    main()
