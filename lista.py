# Lista de exercícios 1

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


""" Usando a definição de conectividade de pixels, faça um programa que conte
automaticamente o número de palitos de fósforo na imagem Fig8.02, informando
também a área (número de pixels) de cada um deles. Seu programa deve fornecer
a área de cada palito (desconsidere a cabeça dos palitos). Observe que você terá
que binarizar a imagem: gere o seu histograma e escolha um valor de limiar para
mapear, acima dele, no nível de cinza 255; e abaixo ou igual a ele, no nível de
cinza 0."""

def histograma(img,bits):
    "Retorna o histograma. Parametos: matriz_imagem; numero de bits"
    bits = bits-1
    lista_bits = list(range(bits))
    qnt = np.zeros(bits)
    for i in lista_bits: 
        qnt[i] = np.count_nonzero(img == i)
        
    plt.bar(lista_bits,qnt)
    return lista_bits, qnt
        
    
def imagemBinaria(img,menor):
    "Transforma em imagem binaria"
    t = len(img)
    imgb = np.zeros((t,t)) #criando vetor vazio do mesmo tamanho da imagem
    for i in range(t):
        for j in range(t):
            if img[i][j] <= menor:
                imgb[i][j] = 0
            else:
                imgb[i][j] = 1
                
    return imgb


##############################################################################
# main #
##############################################################################

img = mpimg.imread('Fig8.02.jpg') #lendo imagem
print(img) #print da imagem em matrix
imgplot = plt.imshow(img, cmap ='gray') #print da imagem como figura
#plt.hist(img) #funcao de histograma

imgb = imagemBinaria(img,127)        
imgplot = plt.imshow(imgb, cmap = 'gray') #print da imagem binaria

# histograma
lista_bits, qnt = histograma(img,256)


    

