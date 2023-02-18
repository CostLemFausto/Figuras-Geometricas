# Desenha figuras geométricas: Linha, Reyângulo, Círculo
# ***************************************************************
import cv2 as cv
# Desenha figuras geométricas: Linha, Retângulo, Círculo.
#***********************************************************************
import numpy as np
# **********************************************************************
img = cv.imread("/home/takion/Documentos/Pixel/clin2.PNG")
img2 = np.copy(img)
#***********************************************************************
def figuras(img2):
    img2 = cv.line(img2,(50,50),(300,50),(0,255,0),3) # Cria linha
    img2 = cv.rectangle(img2,(200,100),(250,150),(200,0,0),3) # retangulo
    img2 = cv.circle(img2,(100,220),(50),(200,0,0),-1) # circulo
    return img2
figuras(img2)
#************************************************************************
cv.imshow("Caso Clinico", img2)
cv.waitKey(0)
cv.destroyAllWindows()