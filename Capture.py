import numpy as np
import cv2
import os
import subprocess
cap = cv2.VideoCapture(0)
counter = 0   
namebool = True

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    while(namebool):
        name = raw_input("Enter the name of the person")
        type(name)
        namebool = False
    path = os.getcwd()
    dirname = path + "/" + name + "_images"
  #  os.chdir(dirname)

    # Display the resulting frame
    #cv2.imshow('frame',gray)
    k = cv2.waitKey(2)
    if k%256 == 49:
        os.mkdir("images")
        os.chdir("images")
    if k%256 == 50:
        os.mkdir(dirname)
    elif k%256 == 27:
    # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
    # SPACE pressed
        print(os.getcwd())
        img_name = "opencv_frame_{}.png".format(counter)
        print(dirname + "/" + img_name)
        cv2.imwrite(dirname + "/" + img_name, frame)
        cv2.imread(dirname + "/" + img_name)
        print("{} written!".format(img_name))
        counter += 1

    #When everything done, release the capture
# if k%256 == 27:
cap.release()
cv2.destroyAllWindows()