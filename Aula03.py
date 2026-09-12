import cv2
import numpy as np

#   Fonte de captura de video
cap = cv2.VideoCapture(0)



while True:
    ret, frame = cap.read()

    if not ret:
        print("Erro de captura")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    vermelhoEscuro = np.array([140, 45, 45])
    vermelhoClaro = np.array([179, 255, 255])

    azulEscuro = np.array([75,45, 45])
    azulClaro = np.array([135, 255, 255])

    verdeEscuro = np.array([20, 35, 35])
    verdeClaro = np.array([95, 255, 255])

    mascaraAzul = cv2.inRange(hsv, azulEscuro, azulClaro)
    mascaraVerd = cv2.inRange(hsv, verdeEscuro, verdeClaro)
    mascaraVerm = cv2.inRange(hsv,vermelhoEscuro, vermelhoClaro)

    # mescla oq fica em branco - tem and, or
    misturaVerm = cv2.bitwise_and(frame, frame, mask = mascaraVerm)
    misturaVerd = cv2.bitwise_and(frame, frame, mask = mascaraVerd)
    misturaAzul = cv2.bitwise_and(frame, frame, mask = mascaraAzul)
    
    cv2.imshow("Filtro R", misturaVerm)
    cv2.imshow("Filtro G", misturaVerd)
    cv2.imshow("Filtro B", misturaAzul)



    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()


