import cv2

img1 = cv2.imread("paisagem.jpg")
img2 = cv2.imread("paisagem.jpg")
# img1[100:150, 150:200] = [0, 0, 255]
# pixel = img1[100, 150]
#print(f"Valor BGR do pixel:{pixel}")

#roi = img1[200:500, 100:300] #Região de interesse

#somaDireta = cv2.add(img1, img2)

mescla = cv2.addWeighted(img1, 0.5, img2, 0.5, 0 )

#cv2.imshow("PaisagemMod", img1)
#cv2.imshow("TrechoPaisa", img2)
#cv2.imshow("somaDireta", somaDireta) #as imagens deve ser do msm tamnaho
cv2.imshow("mesclagem", mescla)

cv2.waitKey(0)
cv2.destroyAllWindows()