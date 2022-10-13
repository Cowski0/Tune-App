import cv2
from PIL import Image
image = cv2.imread("test.png")
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
img = Image.open("test.png")
print(img.getpixel((maxLoc[0],maxLoc[1])))