#Trabalhar filtros para mundo real 
#Diminuir ruidos -> por ex Aula03 q fiz rgb
#Tecnica de convulação

import cv2
import numpy as np

imgs = ['imruido.jpg', 'ruido']
img = cv2.imread(imgs[0])

blur_media = cv2.blur(img, [9, 9])
blur_gaus = cv2.GaussianBlur(img, [9, 9], 0)
blur_mediana = cv2.medianBlur(img, 9)

cv2.imshow('sd',img)
cv2.imshow('blur', blur_media)
cv2.imshow('gaus', blur_gaus)
cv2.imshow('mediana', blur_mediana)



cv2.waitKey(0)
cv2.destroyAllWindows()