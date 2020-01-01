#Authhor:NEEl MACWAN
#instagram @neel_2599
#Open CV Library is used for Image Processing
#OpenCV is a library of programming functions mainly aimed at real-time computer vision. 
# Originally developed by Intel, it was later supported by Willow Garage then Itseez. 
# The library is cross-platform and free for use under the open-source BSD license.
# Definition By Wikipedia
import cv2  
  
# load the required trained XML classifiers 
# Trained XML classifiers describes some features of some 
# object we want to detect a cascade function is trained 
# from a lot of positive(faces) and negative(non-faces) images. 
face_cascade = cv2.CascadeClassifier('C://Users//NEEL//Desktop//Cascade//haarcascade_frontalface_default.xml') 

 
cap = cv2.VideoCapture(0) # captures frames from a camera
  
# loop runs if capturing has been initialized. 
while 1:  
  
    # reads frames from a camera 
    ret, img = cap.read()  
  
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converts Images COlOR to Gray-Scale
  
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # Detects faces of different sizes in the input image 
  
    for (x,y,w,h) in faces: 
        # To draw a rectangle over The Detected Faces 
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 
  
      # Display an image in a window 
    cv2.imshow('img',img) 
  
    # Wait for Esc key to stop 
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
  
# Close the window 
cap.release() 
#instgram: @neel_2599
#instgram: @neel_2599
#instgram: @neel_2599
# De-allocate any associated memory usage 
cv2.destroyAllWindows()  