
import cv2
cap = cv2.VideoCapture(0)
while True:
    success,img = cap.read()
    cv2.imshow("Media Controller", img)
    key = cv2.waitKey(1)
    if key == 32:
        break
        
cv2.destroyAllWindows()       
