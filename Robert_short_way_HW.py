import cv2
import numpy as np
from scipy import ndimage

# Roberts' matrix for X
robertsX = np.array([[1, 0], [0, -1]])
# Roberts' matrix for Y
robertsY = np.array([[0, 1], [-1, 0]])

# Read the image and convert it to gray and then convert the type to float64
img = cv2.imread("bridge.jpg", 0).astype('float64')

# divide the value of img by 255
img /= 255.0
X = ndimage.convolve(img, robertsX)
Y = ndimage.convolve(img, robertsY)

# calculate: |G| = sqrt((GX)^2 + (GY)^2)
edged_img = np.sqrt(np.square(Y) + np.square(X))

cv2.imshow("Original", img)
cv2.imshow("Robert", edged_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
