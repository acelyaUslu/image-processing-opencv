import cv2

# Görüntüyü yükle
image = cv2.imread("cat.jpg")

# Resim bulundu mu kontrol et
if image is None:
    print("Resim bulunamadı!")
    exit()

# Gaussian Blur ile bulanıklaştırma
blurred = cv2.GaussianBlur(image,(5,5),0)

# Kenar algılama (alt ve üst eşik değerleri)
edges = cv2.Canny(blurred, 10, 100)

# Göster
cv2.imshow("Orijinal", image)
cv2.imshow("Kenarlar", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
