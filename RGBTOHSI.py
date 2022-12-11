import cv2
import numpy as np
import math

img = cv2.imread("bridge.jpg")

bgr = np.float32(img) / 255

blue = bgr[:, :, 0]
green = bgr[:, :, 1]
red = bgr[:, :, 2]

# Calculate Intensity (I)
intensity = np.divide(blue + green + red, 3)

# Calculate Saturation (S)
minimum = np.minimum(np.minimum(red, green), blue)
saturation = 1 - (3 / (red + green + blue + 0.001) * minimum)

hue = np.copy(blue)

for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        hue[i][j] = 0.5 * ((red[i][j] - green[i][j]) + (red[i][j] - blue[i][j])) / math.sqrt(
            (red[i][j] - green[i][j]) ** 2 + ((red[i][j] - blue[i][j]) * (green[i][j] - blue[i][j])))

        hue[i][j] = math.acos(hue[i][j])

        if blue[i][j] <= green[i][j]:
            hue[i][j] = hue[i][j]
        else:  # blue[i][j] > green[i][j]
            hue[i][j] = ((360 * math.pi) / 180.0) - hue[i][j]

hsi_img = cv2.merge((hue, saturation, intensity))

cv2.imshow("original", img)
cv2.imshow("HSI", hsi_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
