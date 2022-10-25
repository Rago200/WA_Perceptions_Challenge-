import cv2 as cv
from cv2 import imshow
import numpy as np

# Reading in the image
img = cv.imread("image/red.png")

#converting the 
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# define range of orange traffic cone color in HSV
lower_cone1 = np.array([0, 160, 135])
lower_cone2 = np.array([10, 255, 255])
upper_cone1 = np.array([159, 160, 95])
upper_cone2 = np.array([179, 255, 255])

# Using a mask for the upper and lower threshold
imgThreshLow = cv.inRange(hsv_img, lower_cone1, lower_cone2)
imgThreshHigh = cv.inRange(hsv_img, upper_cone1, upper_cone2)

#combing the lower threshold adn the upper threshold to get all values in range
threshed_img = cv.bitwise_or(imgThreshLow, imgThreshHigh)

#creating a 4 by 4 kernel
kernel = np.ones((4,4),np.uint8)

#eroding and dilating pixels using the kernel with 2 iterations.
threshed_img_smooth = cv.erode(threshed_img, kernel, iterations = 3)
threshed_img_smooth = cv.dilate(threshed_img_smooth, kernel, iterations = 2)

#Using the canny and contours to find the cordinates of the cone.
edges_img = cv.Canny(threshed_img_smooth, 100, 200)
contours, hierarchy = cv.findContours(edges_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#used to store the center x and y values of the cones
center_x = []
center_y = []

#accessing the centers
for i in range(len(contours)):
    if i % 2 == 0:
        M = cv.moments(contours[i])
        center_x.append(int(M["m10"] / M["m00"]))
        center_y.append(int(M["m01"] / M["m00"]))

#hows coordinates to particular lines. 
line_1 = []
line_2 = []

#adding them two the respective lines.
for i in range(len(center_x)):
    if i % 2 == 0:
        line_1.append((center_x[i], center_y[i]))
    else:
        line_2.append((center_x[i], center_y[i]))

#using the coordinates to find the line of best fit
v_x_1, v_y_1, x_1, y_1 = cv.fitLine(np.array(line_1), cv.DIST_L2, 0, 0.01, 0.01)
v_x_2, v_y_2, x_2, y_2 = cv.fitLine(np.array(line_2),  cv.DIST_L2, 0, 0.01, 0.01)

#creating the lines
cv.line(img, (int(x_1 - v_x_1 * 1500), int(y_1 - v_y_1 * 1500)), (int(x_1 + v_x_1 * 1500), int(y_1 + v_y_1 * 1500)), (0, 0, 255), 5)
cv.line(img, (int(x_2 - v_x_2 * 1500), int(y_2 - v_y_2 * 1500)), (int(x_2 + v_x_2 * 1500), int(y_2 + v_y_2 * 1500)), (0, 0, 255), 5)

cv.imshow("Img", img)
cv.imwrite("image/ans.png", img)
cv.waitKey(0)
cv.destroyAllWindows()