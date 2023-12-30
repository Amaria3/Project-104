import cv2
img =cv2.imread("solar-system.jpg")
cv2.imshow("display image",img)
grayscale=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("gray",grayscale)
cv2.waitKey(0)