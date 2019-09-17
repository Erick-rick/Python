print('-- Estacionamento -- ')

he = int(input('Digite a hora de entrada:'))
me = int(input('Digite o minuto de entrada:'))

hs = int(input('Digite a hora de saída:'))
ms = int(input('Digite o minuto de saída:'))

hr = (hs - he) * 4
mn = (ms - me) * 0.10

pag = (hr - mn)

print('O valor é >>> ', pag)





