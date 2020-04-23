import cv2
import numpy as np

cap = cv2.VideoCapture('<video file path>')
frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))

frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

out = cv2.VideoWriter("<video file path>", fourcc, 5.0, (1280,720))

ret, frame1 = cap.read()
ret, frame2 = cap.read()
print(frame1.shape)
while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2) #finding the abs difference between frames
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) #converting RBG to gray
    blur = cv2.GaussianBlur(gray, (5,5), 0) #blur to soften the edges (5,5): kurnel size; 0:sigmax
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) #setting the tresholds
    dilated = cv2.dilate(thresh, None, iterations=3) #dilating the image to fill in the holes in the image to find better contours ie nise whitin the countour
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #mode:cv2.RETR_TREE method:cv2.CHAIN_APPROX_SIMPLE
    cv2.drawContours(frame1,contours,-1,(0,255,0)) #id: -1 color: green0,255,0

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour) #drawing rect

        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255), 3)
  

    image = cv2.resize(frame1, (1280,720))
    out.write(image)
    cv2.imshow("feed", frame1)
    frame1 = frame2 #setting the current frmae as previous frame to compare image
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
out.release()