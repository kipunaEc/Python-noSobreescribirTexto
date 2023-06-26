#importar librerías
import cv2
import numpy as np
#Objeto de video cature
capture = cv2.VideoCapture(0)
#Características del texto
texto = "Valores aleatrios"
ubicacion = (10,100)
ubicacion2 = (10,200)
tipoLetra = cv2.FONT_HERSHEY_TRIPLEX
tamañoLetra = 2
colorLetra = (0,255,0)
grosorLetra = 2

while (capture.isOpened()):
    #Leer cada frame
    ret, frame = capture.read()
    if (ret == True):
        #Texto números aleatorios
        numeros = np.random.rand()
        #Colocar texto
        cv2.putText(frame, texto, ubicacion, tipoLetra, tamañoLetra, colorLetra, grosorLetra)
        cv2.putText(frame, "%.5f" % (numeros), ubicacion2, tipoLetra, tamañoLetra, colorLetra, grosorLetra)
        #Mostrar frames
        cv2.imshow("Video", frame)
        #Al presionar la tecla s sale del bucle
        if (cv2.waitKey(1) == ord('s')):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
