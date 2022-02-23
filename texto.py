#Importar biblioteca openCV
import cv2
import numpy as np
#Leer imagen y redimensionar
img = cv2.imread('Quito.jpg')
img = cv2.resize(img, (720, 570))
#Características del texto
ubicacion = (20,150)
ubicacion2 = (20,300)
tipoLetra = cv2.FONT_HERSHEY_TRIPLEX
tamañoLetra = 1.9
colorLetra = (255,0,0)
grosorLetra = 2
#Escribir numeros del 1 al 20
for i in range(25):
    texto = np.random.rand()
    #Copiar imagen
    img2 = img.copy()
    #Escribir Texto
    cv2.putText(img2, str(texto), ubicacion, tipoLetra, tamañoLetra, colorLetra, grosorLetra)
    cv2.putText(img2, "%.2f[unidades]" % (texto), ubicacion2, tipoLetra, tamañoLetra, colorLetra, grosorLetra)
    #Mostrar imagen
    cv2.imshow('Imagen',img2)
    cv2.waitKey(200)

cv2.destroyAllWindows()
