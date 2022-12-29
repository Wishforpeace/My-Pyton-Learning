from numpy import *
from scipy import *
import numpy as np
from scipy.stats import expon
import cv2

srcImage = cv2.imread("Tommy.jpg")
print(srcImage.shape)

cv2.namedWindow("Original image")
# 显示图像
cv2.imshow("Original image", srcImage)
k = cv2.waitKey(0)

# 灰度处理
print(6666)
grayImage = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)  # 灰度变换
print(grayImage.shape)

cv2.imshow("grayimage", grayImage)
k = cv2.waitKey(0)
# 加入高斯噪声
image = np.array(grayImage / 255, dtype=float)
percent = 0.01
num = int(percent * image.shape[0] * image.shape[1])

for i in range(num):
    temp1 = np.random.randint(image.shape[0])
    temp2 = np.random.randint(image.shape[1])

    mean = 0
    var = 0.04
    noise = np.random.normal(mean, var ** 0.5)
    image[temp1][temp2] += noise
out = image
if out.min() < 0:
    low_clip = -1
else:
    low_clip = 0
out = np.clip(out, low_clip, 1)
gasuss_image = np.uint8(out * 255)
print(gasuss_image.shape)
cv2.imshow("gasuss_image", gasuss_image)
k = cv2.waitKey(0)

# 加入泊松噪声
image = np.array(grayImage, dtype=float)
percent = 0.001  # 图像加入噪声比例
num = int(percent * image.shape[0] * image.shapep[1])
for i in range(num):
    temp1 = np.random.randint(image.shape[0])
    temp2 = np.random.randint(image.shape[1])

    scale = 150
    noise = np.random.poisson(scale, 1)
    image[temp1][temp2] += noise
out = image
if out.min() < 0:
    low_clip = -1
else:
    low_clip = 0

out = np.clip(out, low_clip, 255)
expon_image = np.uint8(out)
print(expon_image.shape)
cv2.imshow("expon_image", expon_image)
k = cv2.waitKey(0)
