print('******************************************')
print('*         Jogo de adivinhação            *')
print('******************************************')

numero_secreto = 12
totalTentativas = 3
rodada = 1

while(totalTentativas > 0):
    chute = int(input('Digite um numero : '))
    print('Você digitou >>>',chute)


    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print('**Você acertou!**')
    elif(maior):
        print('**Você errou!** Seu chute foi maior que o numero secreto***')
    elif(menor):
        print('**O numero que você chutou é menor que o numero secreto!***')


    totalTentativas = totalTentativas - 1
    rodada = rodada + 1
    print('>>>>>Você tem mais {} tentativas\n'.format(totalTentativas))
print ('**Fim de Jogo**')