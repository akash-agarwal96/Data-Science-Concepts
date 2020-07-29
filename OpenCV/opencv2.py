import cv2

img = cv2.imread('flower.JPG')

cv2.imshow('Flower Image',img)

cv2.waitKey(0) #program will stop when any key is pressed
cv2.destroyAllWindows()