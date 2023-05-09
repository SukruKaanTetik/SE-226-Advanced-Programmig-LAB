import cv2


image = cv2.imread('colorful-background-1.jpg')
b, g, r = cv2.split(image)
image_merge = cv2.merge([r, g, b])

image_merge [:,0,:] = 0
cv2.imshow("Final", image_merge)
cv2.waitKey(0)
