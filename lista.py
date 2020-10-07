# Lista de exercícios 1

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np




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

""" Usando a definição de conectividade de pixels, faça um programa que conte
automaticamente o número de palitos de fósforo na imagem Fig8.02, informando
também a área (número de pixels) de cada um deles. Seu programa deve fornecer
a área de cada palito (desconsidere a cabeça dos palitos). Observe que você terá
que binarizar a imagem: gere o seu histograma e escolha um valor de limiar para
mapear, acima dele, no nível de cinza 255; e abaixo ou igual a ele, no nível de
cinza 0."""

img = mpimg.imread('Fig8.02.jpg') #lendo imagem
print(img) #print da imagem em matrix
imgplot = plt.imshow(img, cmap ='gray') #print da imagem como figura

# histograma
lista_bits, qnt = histograma(img,256)


imgb = imagemBinaria(img,160)        
imgplot = plt.imshow(imgb, cmap = 'gray') #print da imagem binaria

#numero de palitos
#contando por transação de pixels
#rodar um vetor no meio da imagem e contar o numero de mudança de pixeis de 0 para 1
y = int(len(imgb)/2) #dividindo o tamanho da imagem por 2
imgp = imgb[y:y+1,:]
imgplot = plt.imshow(imgp, cmap = 'gray') #print da imagem binaria

#logica para contar os palitos
count = 0
for i in range(557):
    pixel = imgp[0,i]
    pixel_novo = imgp[0,i+1]
    if pixel == 0 and pixel_novo == 1:
        #so vou contar se a mudança de pixel for de 0 para 1
        count = count + 1
print("Existem",count,"palitos")

"""2) Use a técnica de fatiamento de níveis de intensidade para realçar a aorta da
figura Fig10.15(a).jpg."""

# para solucionar, basta pegar uma determinada região de pixels e realçar, 
# para isso, pegamos um valor de 150 a 200 e colcoamos todos como 200. assim, 
# a parte dessa região sera destacada

img = mpimg.imread('Fig10.15(a).jpg') #lendo imagem
imgplot = plt.imshow(img, cmap ='gray') #print da imagem como figura

tamanho = img.shape #tamanho[0] - numero de linhas, tamanho[1] - numero de colunas
img2 = np.zeros(tamanho)
for i in range(tamanho[0]):
    for j in range(tamanho[1]):
        pixel = img[i,j]
        if pixel >= 150 and pixel < 200:
            pixel = 200
            img2[i,j]= pixel
        else:
            img2[i,j] = pixel
imgplot = plt.imshow(img2, cmap ='gray') #print da imagem como figura

        
        



