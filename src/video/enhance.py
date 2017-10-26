import cv2
import numpy as np
for i in range(1,4):
    image = cv2.imread(str(i)+".jpg")
    image = cv2.GaussianBlur(image, (3, 3), 0.4)
    M = np.ones(image.shape,dtype="uint8")*32
    added = cv2.add(image,M)
    cv2.imwrite(str(i)+".jpg",added)

