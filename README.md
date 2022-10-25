# WA_Perceptions_Challenge

###Libraries
- OpenCV
- Numpy

###Methodology
I started the project by first watching a Youtube tutorial on OpenCV, since I have not interacted with the library before. After, I looked at the image that was given and identified what color the cones were and defined ranges in HSV for the upper and lower ranges. I converted the image to an HSV image and applied the lower and upper ranges to create thresholds that I applied to the HSV version of the image. I looked at the new image to see if most of the background was gone except for the cones and noticed that was not the case. I looked into using a kernal and then eroding and dialiting the pixels so the only thing that would be left was the orange cones which worked. Then I used the canny edge detector in combination with finding the contours for finding the cones cordinates. I added the centers of the cordintates to the respective lines that they belonged too. This allowed me to create the line of best fit between the cordinates for the two lines of cones.

###Image
![ans](https://user-images.githubusercontent.com/95301146/197832111-fd07eb9b-8aa1-4f9c-82bb-ca3358f1829a.png)
