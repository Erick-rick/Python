import cv2

# Le uma imagem
img = cv2.imread('teste.jpg')
#TESTE.jpg')#, cv2.IMREAD_GRAYSCALE

# Mostra na tela
cv2.imshow('image', img)

#Espera pressionar uma tecla
cv2.waitKey(0)

'''>>>>>>>>>>>>Funcoes.py

# def calcular_media(nota1, nota2):
#   return( nota1+nota2)/2

#>>>>>>>>>>testaFunc.py

import funcoes


n1 = float(input('Nota 1 :'))
n2 = float(input('Nota 2 :'))

result = funcoes.calcular_media(n1, n2)

print(result)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''

#-------Entrada na linha de comando---------------------------------

import numpy as np
#import cv2

#Le a imagem para uma matriz
imagem = cv2.imread("...caminho da/imagem.png")
cv2.imshow('original', imagem)

#Pega as propriedade
altura, largura,bytesPorPixel = np.shape(imagem)

# Percorre toda a imagem
for py in range(0, altura):
    for px in range(0, largura):
        print(imagem[py][px])

#--------Redimensionar uma imagem ------------------

image = cv2.imread('...Caminho/da/imgem.png',cv2.IMREAD_INCHANGED)

cv2.imshow("Imagem original", image)
print ('Dimensoes Originais :', image.shape)

scale_percent = 50 #Porcetagem em relação a imagem original
width = int(image.shape[1] * scale_percent /100)
heigth = int(image.shape[0] * scale_percent /100)
dim = (width, heigth)

#resize image
resized = cv2.resize(image, dim, interpolation =cv2.INTER_AREA )
print('Dimensões Alteradas: ', resized.shape)
cv2.imshow('Imagem redimensionada', resized)

