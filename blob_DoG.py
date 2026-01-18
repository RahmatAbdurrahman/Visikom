import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./images/jalan1.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sigma = 1.6       
k = 1.6            
sigma_k = sigma * k

blur_sigma = cv2.GaussianBlur(gray, (0, 0), sigmaX=sigma)
blur_sigma_k = cv2.GaussianBlur(gray, (0, 0), sigmaX=sigma_k)

dog = cv2.subtract(blur_sigma_k, blur_sigma)
dog_norm = cv2.normalize(dog, None, 0, 255, cv2.NORM_MINMAX)
dog_norm = dog_norm.astype(np.uint8)
_, dog_thresh = cv2.threshold(dog_norm, 200, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(
    dog_thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

blob_vis = img_rgb.copy()

for cnt in contours:
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    # if radius > 1:  # filter very small blobs
    center = (int(x), int(y))
    radius = int(radius)
    cv2.circle(blob_vis, center, radius, (255, 0, 0), 5)

plt.figure(figsize=(15, 5))

plt.subplot(2, 2, 1)
plt.imshow(dog, cmap='gray')
plt.title("Difference of Gaussian (DoG)")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(dog_thresh, cmap='gray')
plt.title("Thresholded DoG (Blob Candidates)")
plt.axis('off')

plt.subplot(2, 2, (3, 4))
plt.imshow(blob_vis)
plt.title("Detected Blobs (Circles)")
plt.axis('off')

plt.tight_layout()
plt.show()