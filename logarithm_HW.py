import cv2
import numpy as np
from math import log

img = cv2.imread("bridge.jpg" , 0)  # cv2.COLOR_GRAYSCALE

# uzun yontem
# c = 255 / np.log(1 + np.max(img))
# print(img.shape)
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         # print(img[i,j])
#         img[i,j] = c * log(img[i,j]+1,10) #
#
# kisa yontem
c = 255 / np.log(1 + np.max(img))

logarithm = c * (np.log(img + 1))
logarithm = np.array(logarithm, dtype=np.uint8)

cv2.imshow("Original", img)
cv2.imshow("logarithm", logarithm)
cv2.waitKey(0)
cv2.destroyAllWindows()
