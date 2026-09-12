import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cv2.imread()
    if not ret:
        print("Erro")
        break

    cv2.imshow(frame)

    if cv2.waitKey(1) & 0XFF == ord('q')