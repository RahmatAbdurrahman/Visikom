# # SIFT (Scale-Invariant Feature Transform)

# ## Import resources and display image

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
img1 = cv2.imread('./images/jalan1.jpg')
img2 = cv2.imread('./images/jalan2.jpg')

# Convert BGR to RGB (for matplotlib)
img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()

kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

print("Keypoints img1:", len(kp1))
print("Keypoints img2:", len(kp2))

bf = cv2.BFMatcher(cv2.NORM_L2)

matches = bf.knnMatch(des1, des2, k=2)

good_matches = []
ratio = 0.75
for m, n in matches:
    if m.distance < ratio * n.distance:
        good_matches.append(m)

print("Good matches:", len(good_matches))

matched_img = cv2.drawMatches(
    img1_rgb, kp1,
    img2_rgb, kp2,
    good_matches[:100], None,
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

plt.figure(figsize=(14, 7))
plt.imshow(matched_img)
plt.axis('off')
plt.title("SIFT Feature Matching")
plt.show()