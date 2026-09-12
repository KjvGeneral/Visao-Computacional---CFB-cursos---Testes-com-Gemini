import cv2
import numpy as np
import math as mt

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("\n Erro de captura")
        break

    # Processamento de imagem para a escala HSV
    Blur = cv2.medianBlur(frame, 9)
    hsv = cv2.cvtColor(Blur, cv2.COLOR_BGR2HSV)

    # Definição de qual cor queremos criar uma mascara para depois rastrear
    claro  = np.array([35, 45, 45])
    escuro = np.array([79, 255, 500])

    # Criamo uma mascara para separamos qual cor queremos para qual não queremos
    # Nesse caso, tudo que não queremos vira preto e tudo que queremos vira branco
    mask =  cv2.inRange(hsv, claro, escuro)
    

    # Agora vem a parte com ajuda do gemini
    # Vamos usar uma nova função "cv2.findCoutours()" que vai estar dentro de uma variavael chamada 
    # contorno, e uma segunda que e omitida que recebe uma hieraquia que não vamos usar
    contorno, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Vamos pegar apenas a maior mancha branca, ignorando os ruidos
    if contorno:
        maior_contorno = max(contorno, key=cv2.contourArea)

        area_min = 200
        area_max = 10000000000

        # Vamos perguntar se maior matriz que lemos da mancha branca e maior que o numero de pexeis
        # Vamos detectar varios objetos

        for objeto in contorno:
            area = cv2.contourArea(objeto)

            if area_min < area < area_max:
                x, y, l, h = cv2.boundingRect(objeto)

                cv2.rectangle(frame, (x, y), (x+l, y+h), (0, 255, 0), 2)
                cv2.rectangle(mask, (x, y), (x + l, y + h), 255, 2)
                cv2.putText(frame, "Obj Detectado", (x -150, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.putText(mask, "Obj Detectado", (x -150, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, 255, 2)

    cv2.imshow("Mascara", mask)
    cv2.imshow("VideoHSV",frame)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        print("\n Fim de programa \n")
        break


cap.release
cv2.destroyAllWindows()
