import cv2
import numpy as np
img = cv2.imread("test.jpg")

window_name = 'something'

print(img.shape)
print(img[100][100])

cv2.imshow(window_name, img)

window_name = 'warped'

M = np.float32([
	[1, 0, 3],
	[0, 1, 3]
])

img2 = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow(window_name, img2)

window_name = 'subtract'

img3 = cv2.subtract(img, img2)

cv2.imshow(window_name, img3)


cv2.waitKey(0)






# closing all open windows
cv2.destroyAllWindows()