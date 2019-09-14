import sys #Função do sistema
import string 

texto = input('Digite a mesagem a ser criptografada ou descifrada: ')
texto = texto.upper()

chave = int(input('Digite o valor da chave/deslocamento: '))

modo = input('Escolha E para encriptar ou  D para decriptar :')

CARACTERES= 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'

convertido = ''

for caractere in texto:
    if caractere in CARACTERES:
        num =CARACTERES.find(caractere)
    if modo == 'E':
        num = num + chave
    elif modo == 'D':
        num = num - chave

    if num >= len(CARACTERES):
        num = num - len(CARACTERES)
    elif num < 0 :
        num = num + len(CARACTERES)
        convertido = convertido + CARACTERES[num]
    else:
        convertido = convertido + caractere
    
    if modo == 'E':
        print ('O texto criptografado é ', convertido)
    
    if modo == 'D':
        print ('O texto descriptado é ', convertido)
