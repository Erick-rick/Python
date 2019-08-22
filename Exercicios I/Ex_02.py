print ('Área e perimetro de uma sala')

L = int(input('Digite a largura da sala :'))
C = int(input('Digite o comprimento da sala:'))

area = L * C
perimetro = 2*(L + C)

print ('O tamanho da área é : {} M².\nÉ o perimetro de :{}'.format(area, perimetro))