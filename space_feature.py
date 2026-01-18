import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./images/jalan1.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur_sigma1 = cv2.GaussianBlur(gray, (0, 0), sigmaX=1)
blur_sigma3 = cv2.GaussianBlur(gray, (0, 0), sigmaX=3)
blur_sigma5 = cv2.GaussianBlur(gray, (0, 0), sigmaX=5)

plt.figure(figsize=(15, 5))

plt.subplot(2, 2, 1)
plt.imshow(gray, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(blur_sigma1, cmap='gray')
plt.title("Gaussian Blur σ = 1")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(blur_sigma3, cmap='gray')
plt.title("Gaussian Blur σ = 3")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(blur_sigma5, cmap='gray')
plt.title("Gaussian Blur σ = 5")
plt.axis('off')

plt.tight_layout()
plt.show()
