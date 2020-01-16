#Manipulação de Texto
# 
# Fatiamento
# 
# frase = 'Curso em Video python'
# 
# frase[9] = V
# frase[9:13] = Vide **( não pegando caracter 13, smp um a menos)
# frase[9:21:2] = Vdo pto (pulando de 2 em 2)
# frase[:5] = Curso (do inicio até o 5)
# frase[15:] = python(do 15 ate o final da string)
# frase[9::3] = veph   (começa do 9 até o final)

#Analise
# len(frase) > comprimento da frase 21 caracters
# frase.count('o')  > contar quantas x aparece a letra 'o' na frase 
# frase.find('deo') > encontra as string 'deo' a posição 11
# frase.find('android') > devolvendo -1 não existe na frase
# 'Curso' in frase > Encontra a palavra na frase
# 

#Transformação
# frase.replace('Python', 'Android')##