import cv2
import matplotlib.pyplot as plt

psf = cv2.imread("./psf.tiff", cv2.IMREAD_GRAYSCALE).astype(float) / 255
psf[psf < 0.2] = 0
cv2.imwrite("./filtered_psf.png", psf * 255)
plt.imshow(psf, cmap='gray')
plt.show()
