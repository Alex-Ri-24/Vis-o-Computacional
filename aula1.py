import cv2

# Exercício 1: Selecione uma imagem qualquer e recorte uma região desejada da
#imagem, conforme exemplo abaixo.
imagem = cv2.imread('camaro.png')
recorte = imagem[50:200, 50:200]
cv2.imshow("Imagem", imagem)
cv2.imshow("Região Recortada", recorte)
cv2.waitKey(0)

# Exercício 2: Salve uma imagem com uma borda, conforme exemplo abaixo. Mudando somente a cor dos pixels da imagem
borda = imagem

for linha in range (0, borda.shape[0]):
    for coluna in range (0, borda.shape[1]):
        if linha < 100 or linha > borda.shape[0] - 100 or coluna < 100 or coluna > borda.shape[1] - 100:
            borda[linha, coluna] = (255, 0, 0) 
cv2.imshow("Imagem com Borda", borda)
cv2.waitKey(0)

# exercício 3: Salve uma imagem em escala de cinza com uma borda cinza, conforme exemplo abaixo.

image_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem em Escala de Cinza", image_gray)
cv2.waitKey(0)

# exercício 4: Salve uma imagem com um quadrado em cada borda, conforme exemplo abaixo.

imagem = cv2.imread('camaro.png')
for L in range(0, 100): #primeiro quadrado superior esquerdo
    for C in range(0, 100):
        imagem[L, C] = (0, 0, 255)

for L in range(0, 100): #segundo quadrado superior direito
    for C in range(imagem.shape[1] - 100, imagem.shape[1]):
        imagem[L, C] = (0, 0, 255)

for L in range(imagem.shape[0] - 100, imagem.shape[0]): #terceiro quadrado inferior esquerdo
    for C in range(0, 100):
        imagem[L, C] = (0, 0, 255)

for L in range(imagem.shape[0] - 100, imagem.shape[0]): #quarto quadrado inferior direito
    for C in range(imagem.shape[1] - 100, imagem.shape[1]):
        imagem[L, C] = (0, 0, 255)

cv2.imshow("Imagem com Quadrados", imagem)
cv2.waitKey(0)

# exercício 5: Salve uma imagem com um quadrado escondendo o rosto dapessoa, conforme exemplo abaixo.
rosto = cv2.imread('ted_mosby.jpeg')

for L in range(rosto.shape[0] - 300, rosto.shape[0]-100):
    for C in range(rosto.shape[1] - 300, rosto.shape[1]-100):
        rosto[L, C] = (0, 0, 255)

cv2.imshow("Cobre o rosto do Ted Mosby", rosto)
cv2.waitKey(0)

# exercício 6: Salve uma imagem com uma outra imagem no início (posição 0,0), conforme exemplo abaixo.
imagem1 = cv2.imread('camaro.png')
imagem2 = cv2.imread('ted_mosby.jpeg')

# Copiar a segunda imagem para a primeira imagem, na posição (0,0)
for L in range(imagem2.shape[0]):
    for C in range(imagem2.shape[1]):
        imagem1[L, C] = imagem2[L, C]

cv2.imshow("Imagem com Outra Imagem", imagem1)
cv2.waitKey(0)

# exercício 7: Salve uma imagem com uma outra imagem embaixo no canto direito, conforme exemplo abaixo.
imagem1 = cv2.imread('camaro.png')
imagem2 = cv2.imread('ted_mosby.jpeg')

# Copiar a segunda imagem para a primeira imagem, no canto inferior direito
for L in range(imagem2.shape[0]):
    for C in range(imagem2.shape[1]):
        imagem1[L + imagem1.shape[0] - imagem2.shape[0], C + imagem1.shape[1] - imagem2.shape[1]] = imagem2[L, C]

cv2.imshow("Imagem com Outra Imagem", imagem1)
cv2.waitKey(0)

