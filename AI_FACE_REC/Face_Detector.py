import cv2
from random import randrange

# Load some pre-trained data on face frontals from opencv
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Choose an image to detect face 
img = cv2.imread("R_D_JR.png")


# Convert the image to black and white
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# Draw rectangles around the faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w,x+h), (randrange(128, 256), randrange(128, 256), randrange(128, 256)), 5)

#code below is a manual iteration of all the images
#(x, y, w, h) = face_coordinates[0]
#cv2.rectangle(img, (x, y), (x+w,y+h), (0, 255, 0), 5)


# image of the code
cv2.imshow("Face Detector", img)

# pauses execution of the code until a key is pressed
cv2.waitKey()

print("Code Complete")
