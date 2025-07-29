import cv2

image = cv2.imread("cat.jpg")

if image is None:
    print("Resim bulunamadı.")
    exit()

#Gaussian Blur

blurred = cv2.GaussianBlur(image,(65,65),0)

cv2.imshow("Original",image)
cv2.imshow("Gaussian Blur", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()