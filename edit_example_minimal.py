import cv2

img = cv2.imread("lena.jpg")
cv2.imshow("test_win", img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

import matplotlib.pyplot as plt

plt.imshow(img)
plt.show()
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
quit()