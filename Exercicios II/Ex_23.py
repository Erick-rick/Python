
dc = 0

dc = float(input('Digite a distancia do cruzamento :\n '))

if (dc == 0):
    cs = '>>>> Vermelho - PARAR!'
elif (dc <= 5):
    cs = '>>>> Amarelo - PASSAR COM CUIDADO!'
elif(dc >= 5 ):
    cs = '>>>>Verde - PASSAR'

print ('Distancia indicada : {} \n Semaforo : {} \n'.format(dc, cs))