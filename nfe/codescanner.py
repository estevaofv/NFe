from __future__ import print_function
import pyzbar.pyzbar as pyzbar # pip install pyzbar
import numpy as np #pip install numpy
import cv2 #pip install opencv-python

# Ainda vou atualizar muita coisa(acho), só dei um commit parcial mesmo

def decode(im):
    # Decodifica(pode ser QRCode ou código de barras)
    decodedObjects = pyzbar.decode(im)

    # Imprime resultados
    for obj in decodedObjects:
        print('Tipo: ', obj.type)
        print('Dados: ', obj.data, '\n')

    return decodedObjects


# Mostra a localização do QRCode ou do código de barras
def display(im, decodedObjects):
    # Pega objetos decodificados
    for decodedObject in decodedObjects:
        points = decodedObject.polygon

        # Se pontos não formam quatro lados, tenta achar a 'casca convexa'
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points;

        # Número de pontos na casca convexa
        n = len(hull)

        # Desenha a casca convexa
        for j in range(0, n):
            cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

    # Mostra resultados
    cv2.imshow("Results", im);
    cv2.waitKey(0);


# Main
if __name__ == '__main__':
    # Lê a imagem
    im = cv2.imread('codigo2.png')

    decodedObjects = decode(im)
    display(im, decodedObjects)
