import cv2
import numpy as np

img_1 = cv2.imread("bridge.jpg",0)
c = 1
img = np.zeros(img_1.shape , dtype="uint8")
gamma = [3,4,5]
# uzun yontem
# for gm in gamma:
#     for i in range(img_1.shape[0]):
#         for j in range(img_1.shape[1]):
#             img[i,j] = c * (img_1[i,j] ** gm)
#     cv2.imshow(f"for{gm} value of gama",img)
#     img = np.zeros(img_1.shape , dtype="uint8")

# kisa yontem
img_2 = c * np.power(img_1, gamma[0])

img_3 = c * np.power(img_1, gamma[1])

img_4 = c * np.power(img_1, gamma[2])

cv2.imshow("Original", img_1)
cv2.imshow("Gamma 3", img_2)
cv2.imshow("Gamma 4", img_3)
cv2.imshow("Gamma 5", img_4)

cv2.waitKey(0)
cv2.destroyAllWindows()
