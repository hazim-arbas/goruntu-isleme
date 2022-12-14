import cv2
import numpy as np

img = cv2.imread("bridge.jpg", 0)

img8 = (img/256).astype('uint8')

cv2.imshow("16",img)
cv2.imshow("8",img8)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
# from skimage import io
# from pyxelate import Pyx, Pal
#
# #load image with 'skimage.io.imread()'
#
# image = io.imread("bridge.jpg")
# downsample_by = 14  # new image will be 1/14th of the original in size
# palette = 7  # find 7 colors
#
# #1) Instantiate Pyx transformer
#
# pyx = Pyx(factor=downsample_by, palette=palette)
#
# #2) fit an image, allow Pyxelate to learn the color palette
#
# pyx.fit(image)
#
# #3) transform image to pixel art using the learned color palette
#
# new_image = pyx.transform(image)
# # save new image with 'skimage.io.imsave()'
# io.imsave("pixel.png", new_image)
