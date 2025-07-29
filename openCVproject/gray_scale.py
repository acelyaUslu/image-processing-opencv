import cv2 # opencv library

image = cv2.imread("cat.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()