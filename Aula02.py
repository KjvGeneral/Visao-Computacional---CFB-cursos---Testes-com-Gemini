import cv2

#Cap = captura      0 = webcam
cap = cv2.VideoCapture(0)
largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
altura  = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = cv2.VideoWriter_fourcc(*'XVID')

# gravador de webCam
# nome do arquivo, codec, Framerate, Tamanho Largura e altura
gravador = cv2.VideoWriter("videoTest.avi", codec, 24,(largura, altura))

#construção do loop
while True:
# bool   img
    ret, frame = cap.read()
    frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Conversão para escala de cinza

    gravador.write(frame)

    if not ret:
        print("Erro na captura")
        break #sai do loop caso erro

    #cv2.imshow("VideoRGB", frame) #video em rgb ou em openCV BGR
    cv2.imshow("VideoCV", frame)

    # não sei oq iso quer dizer msm
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release() #desliga webcam
gravador.release() #desliga gravador
cv2.destroyAllWindows()