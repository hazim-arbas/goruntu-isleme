import cv2
import numpy as np

x = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
y = [1, 2, 1, 0, 0, 0, -1, -2, -1]

img = cv2.imread("bridge.jpg")
imgGX = np.zeros((img.shape[:]), dtype=np.uint8)
imgGY = np.zeros((img.shape[:]), dtype=np.uint8)
imgGXY = np.zeros((img.shape[:]), dtype=np.uint8)

# 1'den baslar cunku kenarlari alicaz
for i in range(1, img.shape[0] - 1):
    for j in range(1, img.shape[1] - 1):
        renk = img[i - 1, j - 1].tolist()  # B G R (-1,-1) indexteki deger
        P0 = (renk[0] + renk[1] + renk[2]) // 3

        renk = img[i - 1, j].tolist()  # B G R (-1,0) indexteki deger
        P1 = (renk[0] + renk[1] + renk[2]) // 3

        renk = img[i - 1, j + 1].tolist()  # B G R (-1,+1) indexteki deger
        P2 = (renk[0] + renk[1] + renk[2]) // 3

        renk = img[i, j - 1].tolist()  # B G R (0,-1) indexteki deger
        P3 = (renk[0] + renk[1] + renk[2]) // 3

        renk = img[i, j].tolist()  # B G R (0,0) indexteki deger
        P4 = (renk[0] + renk[1] + renk[2]) // 3

        renk = img[i, j + 1].tolist()  # B G R (0,1) indexteki deger
        P5 = (renk[0] + renk[1] + renk[2]) // 3

        renk = img[i + 1, j - 1].tolist()  # B G R (1,-1) indexteki deger
        P6 = (renk[0] + renk[1] + renk[2]) // 3

        renk = img[i + 1, j].tolist()  # B G R (1,0) indexteki deger
        P7 = (renk[0] + renk[1] + renk[2]) // 3

        renk = img[i + 1, j + 1].tolist()  # B G R (+1,+1) indexteki deger
        P8 = (renk[0] + renk[1] + renk[2]) // 3

        GX = int(
            abs(P0 * x[0] + P1 * x[1] + P2 * x[2] + P3 * x[3] + P4 * x[4] + P5 * x[5] + P6 * x[6] + P7 * x[7] + P8 * x[
                8]))

        GY = int(
            abs(P0 * y[0] + P1 * y[1] + P2 * y[2] + P3 * y[3] + P4 * y[4] + P5 * y[5] + P6 * y[6] + P7 * y[7] + P8 * y[
                8]))

        GXY = GX + GY

        if GX > 255:
            GX = 255
        if GY > 255:
            GY = 255
        if GXY > 255:
            GXY = 255
        imgGX[i, j] = [GX, GX, GX]
        imgGY[i, j] = [GY, GY, GY]
        imgGXY[i, j] = [GXY, GXY, GXY]

cv2.imshow("Original", img)
cv2.imshow("GX", imgGX)
cv2.imshow("GY", imgGY)
cv2.imshow("GXY", imgGXY)

cv2.waitKey(0)
cv2.destroyAllWindows()
