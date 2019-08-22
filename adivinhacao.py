print('******************************************')
print('*       Jogo de adivinhação              *')
print('******************************************')

numero_secreto = 12

chute = int(input('Digite um numero : '))
print('Você digitou >>>',chute)

if (numero_secreto == chute):
    print('**Você acertou!**')
elif(chute > numero_secreto):
    print('**Você errou!** Seu chute foi maior que o numero secreto***')
elif(chute < numero_secreto):
    print('**O numero que você chutou é menor que o numero secreto!***')