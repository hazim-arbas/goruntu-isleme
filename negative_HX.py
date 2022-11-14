import cv2 as cv2
import numpy as np

img = cv2.imread("bridge.jpg")
img_neg = np.zeros(img.shape[:], dtype="uint8")

# LONG method to convert image to negative
# This method is not for gray images
height, width, _ = img.shape
pixel = []
for i in range(height):
    for j in range(width):
        pixel[:] = img[i, j,:]
        pixel[0] = 255 - pixel[0] - 1
        pixel[1] = 255 - pixel[1] - 1
        pixel[2] = 255 - pixel[2] - 1
        img_neg[i, j] = pixel

# SHORT method to convert image to negative
# This method is for both gray and color images
img_neg1 = 255 - img - 1

cv2.imshow("Original", img)
cv2.imshow("Negative_longMethod", img_neg)
cv2.imshow("negative_shortMethod", img_neg1)
cv2.waitKey(0)
cv2.destroyAllWindows()
