import cv2 
videocap = cv2.VideoCapture('video.avi')  
cascade_car = cv2.CascadeClassifier('cars.xml') 
 
while True: 
    retvalue, frames = videocap.read() 
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) 
    cars = cascade_car.detectMultiScale(gray, 1.1, 1) 

    for (x,y,w,h) in cars: 
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2) 
    cv2.imshow('Vehicle Detection', frames) 

    if cv2.waitKey(1) & 0xff == ord('q'): 
        break

videocap.release()
cv2.destroyAllWindows() 