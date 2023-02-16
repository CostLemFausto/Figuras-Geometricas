import cv2 as cv
import numpy as np

img = cv.imread("/home/takion/Documentos/Pixel/clin2.PNG")
img2 = np.copy(img)

img2 = cv.line(img,(50,50),(300,50),(0,255,0),3) # Cria linha

img2 = cv.rectangle(img,(200,100),(250,150),(200,0,0),3) # cria retangulo

img2 = cv.circle(img,(100,220),(50),(200,0,0),-1) # cria circulo

cv.imshow("Caso Clinico", img2)

cv.waitKey(0)
cv.destroyAllWindows()