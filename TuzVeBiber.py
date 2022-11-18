
import random
import cv2
import matplotlib.pyplot as plt

realImg = cv2.imread("bridge.jpg", cv2.IMREAD_GRAYSCALE)
noiseImg = cv2.imread("bridge.jpg", cv2.IMREAD_GRAYSCALE)


height, width = noiseImg.shape
# number of pixels that will change
number_of_pixels_to_change = random.randint(500,10000)
for i in range(number_of_pixels_to_change):
    h = random.randint(0,height-1)
    w = random.randint(0,width-1)
    noiseImg[h,w] = 255  # add white color at random index
for i in range(number_of_pixels_to_change):
    h = random.randint(0,height-1)
    w = random.randint(0,width-1)
    noiseImg[h,w] = 0  # add black color at random index

# calculate the histogram
# calcHist(gray image , channel(for colors), mask , histSize , ranges)
histForRealImage = cv2.calcHist(realImg, [0], None, [256], [0, 256])
histForNoiseImage = cv2.calcHist(noiseImg, [0], None, [256], [0, 256])

# plot the image and histogram
fig = plt.figure()

fig.add_subplot(221)
plt.title(' Real Image ')
plt.set_cmap('gray')
plt.imshow(realImg)

fig.add_subplot(222)
plt.title('histogram ')
plt.plot(histForRealImage)

fig.add_subplot(223)
plt.title(' Noise image ')
plt.set_cmap('gray')
plt.imshow(noiseImg)

fig.add_subplot(224)
plt.title('histogram ')
plt.plot(histForNoiseImage)

fig.tight_layout()
plt.show()
