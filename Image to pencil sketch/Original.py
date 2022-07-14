import cv2
import matplotlib.pyplot as plt
plt.style.use('seaborn')
img = cv2.imread("image.jpeg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.axis("off")
plt.title("Original Image")
plt.show()