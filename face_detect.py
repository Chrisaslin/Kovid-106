
import cv2

img = cv2.imread("C:/Users/91880/Downloads/PRO-C106-Reference-Code-main (1)/PRO-C106-Reference-Code-main/boy.jpg")

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('C:/Python310/Lib/site-packages/opencv-4.x/data/haarcascades/haarcascade_frontalface_alt.xml')

faces = face_cascade.detectMultiScale(gray,1.1, 5)

print(len(faces))

for (x,y,w,h) in faces:
       
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  

       # Crop the image to save the face image.
       roi_color = img[y:y+h, x:x+w]
       cv2.imwrite("face.jpg",roi_color)
              
cv2.imshow('img',img)
cv2.waitKey(0)



