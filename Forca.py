
def jogar():
    print('*******************************')
    print('******Jogo da Forca ***********')
    print('*******************************')

    palavra_secreta = 'Apple'
    letras_acertadas = ['_', '_', '_', '_', '_']
    acertou = False
    enforcou = False
    erros = 0

    print (letras_acertadas)

    while (not enforcou and not acertou):
        print('**** Jogando *****\n')

        chute = input('>>>>Qual letra? \n')
        if (chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas [posicao] = letra
                    #print (letras_acertadas)
                    posicao = index + 1
        else:
            erros += 1

        enforcou = erros = 5
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

        if (acertou):
            print('*** You Winner!! ****')
        else:
            print('***You lose !!****')

    print ('***Fim de Jogo***')



