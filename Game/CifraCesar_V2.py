mensagem = input('Digite sua mensagem :\n')

chave = int(input('Digite a chave de codificação :\n'))

def cifra(mensagem, chave):
    cifrado = " "
    for letra in mensagem:
        if letra.isalpha():
            letra = letra.lower()
            numero= ord(letra)+ chave
            if numero > ord('z'):
                numero -=26
                novaLetra = chr(numero)
                if letra == " ":
                    cifrado +=" "
                else:
                    cifrado += novaLetra
    print('A mensagem codificada é : ', cifrado)
    return cifrado

def decifrar(mensagem, chave):
    decifrado =" "
    for letra in mensagem:
        if letra.isalpha():
            numero = ord(letra) - chave 
            if numero < ord('a'):
                numero +=26
                letraOriginal = chr(numero)
            else:
                decifrado+= letraOriginal
                print('A mensagem decodificada é :',decifrado)

codificada = cifra(mensagem, chave)

escolha = input ('Deseja decodificar a mensagem ?')

if escolha == 's' or 'sim':
    chave = int(input('Digite a chave secreta :'))
    decifrar(codificada, chave)