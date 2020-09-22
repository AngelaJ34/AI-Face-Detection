# Overview

 This AI face detection program using images to detect similar facial structures of different faces. Haar Cascade which is named after Haar who created the cascade algorithm filters down until it finds an image to best resembles a person within a rectangle. Haar features are the rudimentary blocks that allow this alogrithm used to capture the likeness of a face using edge, line, and four-rectangle features. These features depend on gray scaled images because it is able to pick up the light and dark areas of a person in an image.


<b> 1. Instructions For Installation </b>

Install the latest version of Python to your operating system of choice before running this program.

Python Website Link: https://www.python.org

Please download all image files and videos links for this project found in the src folder

<b> 2. Packages Required </b>

 # Computer vision package

1.) Implement this command in terminal:

pip3 install opencv-python

OR

pip3 install opencv-python-headless

2.) Implement computer vision 2 command in terminal:

import cv2

This command above checks to ensure you installed the following without error

# Machine Learning Files(Haar Cascade xml files)

Faces Detector XML:https://github.com/opencv/opencv/tree/master/data/haarcascades


# Video of Frontal Face View (Haar Cascade Algorithm Visualization):

Link: https://www.youtube.com/watch?v=hPCTwxF0qf4

# Dataset

OpenCV Documentation:
https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html?highlight=.cvtcolor#cv2.cvtColor

Haarcascade Frontal Face:
https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml

# Run Program Instructions

1.) Once all necessary files are downloaded, open terminal and change directory into folder
<p>
2.) Ensure the proper version of python is running once inside the folder
<p>
3.) Then type ls in terminal to ensure you are in the correct directory and can see all file
<p>
4.) In terminal type in: python3 Face_Detector.py to run the program
<p>
5.) To quit out press control + C  in terminal to stop the program
<p>
