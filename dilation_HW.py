import cv2
import numpy as np

img = cv2.imread('plaka.png', 0).astype(float) // 255

kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
dilation = img.copy()

for i in range(1, img.shape[0] - 1):
    for j in range(1, img.shape[1] - 1):

        # dilated_pixel = np.max(img[i-1:i+2, j-1:j+2] * kernel)
        dilated_pixel = \
            img[i - 1][j - 1] * kernel[0][0] + \
            img[i - 1][j] * kernel[0][1] + \
            img[i - 1][j + 1] * kernel[0][2] + \
            img[i][j - 1] * kernel[1][0] + \
            img[i][j] * kernel[1][1] + \
            img[i][j + 1] * kernel[1][2] + \
            img[i + 1][j - 1] * kernel[2][0] + \
            img[i + 1][j] * kernel[2][1] + \
            img[i + 1][j + 1] * kernel[2][2]
        if dilated_pixel > 0:
            dilation[i][j] = 1
        else:
            dilation[i][j] = 0
        dilation[i][j] = dilated_pixel

cv2.imshow('Original Image', img)
cv2.imshow('Dilation Image', dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
