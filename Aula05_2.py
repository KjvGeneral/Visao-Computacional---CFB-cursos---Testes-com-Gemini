import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        print("Erro de camera")
        break

    
    blur_gaus = cv2.medianBlur(frame, 9)

    hsv = cv2.cvtColor(blur_gaus, cv2.COLOR_BGR2HSV)

    verdeEscuro = np.array([20, 35, 35])
    verdeClaro = np.array([95, 255, 255])
        
    mascaraVerd = cv2.inRange(hsv, verdeEscuro, verdeClaro)

    misturaVerd = cv2.bitwise_and(blur_gaus, blur_gaus, mask = mascaraVerd)

    cv2.imshow("Video", frame)
        
    cv2.imshow("Filtro",misturaVerd)
        

    if cv2.waitKey(1) & 0XFF == ord('q'):
        print("frim de programa")
        break
    
    
print(frame)
cap.release()
cv2.destroyAllWindows()