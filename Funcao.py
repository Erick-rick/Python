

def velocidade(espaco, tempo):
    v = espaco/ tempo
    print('velocidade : {} m/s'.format(v))


#parametros de função
#
def dados(nome, idade =None):
    print('nome: {}'.format(nome))
    if (idade is not None):
        print('idade {}'.format(idade))
    else:
        print('idade : não informada')

#Função com retorno

def velocidade1(espaco, tempo):
    v1 = espaco / tempo
    return v1

def calculadora (x, y):
    return {'Soma ':x + y, 'Subtraçao':x - y}
    
    resultados = calculadora(1,2)
    for key in resultados:
        print('{}: {}'.format(key, resultados[key]))
        
