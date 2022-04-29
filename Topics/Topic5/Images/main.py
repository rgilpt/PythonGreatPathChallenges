import cv2

img = cv2.imread("download.jpg")

window_name = 'image'

print(img.shape)

cv2.imshow(window_name, img)

cv2.waitKey(0)




print(img[2])

# closing all open windows
cv2.destroyAllWindows()