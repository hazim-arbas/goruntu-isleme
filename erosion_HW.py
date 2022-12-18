import cv2
import numpy as np

img = cv2.imread('plaka.png', 0).astype(float) // 255

kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
erosion = img.copy()

for i in range(1, img.shape[0] - 1):
    for j in range(1, img.shape[1] - 1):

        # eroded_pixel = np.min(img[i-1:i+2, j-1:j+2] * kernel)
        eroded_pixel = \
            img[i - 1][j - 1] * kernel[0][0] + \
            img[i - 1][j] * kernel[0][1] + \
            img[i - 1][j + 1] * kernel[0][2] + \
            img[i][j - 1] * kernel[1][0] + \
            img[i][j] * kernel[1][1] + \
            img[i][j + 1] * kernel[1][2] + \
            img[i + 1][j - 1] * kernel[2][0] + \
            img[i + 1][j] * kernel[2][1] + \
            img[i + 1][j + 1] * kernel[2][2]
        if eroded_pixel == 5:
            erosion[i][j] = 1
        else:
            erosion[i][j] = 0

# İşlem sonucunu göster


cv2.imshow('Original Image', img)
cv2.imshow('Erosion Image', erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
