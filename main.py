from PIL import Image
import numpy as np
#importando as bibliotecas utilizadas

# tranformando a imagem para RGB, para certificar-se de que os pixels sejam apresentados neste formato
im = Image.open('Syngenta.bmp').convert('RGB')



# Criando um array de numeros (RGB) da imagem utilizando o numpy
na = np.array(im)



colours, counts = np.unique(na.reshape(-1,3), axis=0, return_counts=1)
# o comando reshape é executado na matriz (na) de números da imagem
#no reshape(-1,3) transformo em um array de três elementos, cada pixel do RGB é colocado junto neste array

#o np.unique percorre minha matriz e ve quantas vezes determinados numeros (em RGB) apareceram
#Eu envio para o return_counts a requisição para ele me retornar o "contador" de cada cor (RGB) contada na imagem.


#printar as cores presentes na imagem em R G B
print(colours)
#printar os contadores de cada cor presente, respectivamente.
print(counts)
#printar os dados da imagem para comparação de pixels
print(im)