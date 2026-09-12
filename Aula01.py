import cv2 
imagem = cv2.imread("teste.jpg") #Leitura de matriz da imagem
cv2.imshow('CursoVC', imagem) #print da imagem
cv2.waitKey(0) #Espera de botão
cv2.destroyAllWindows()#Limpa memoria
print(imagem.shape)

