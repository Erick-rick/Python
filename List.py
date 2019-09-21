meses = ['janeiro', 'Fevereiro', 'março', 'Abril', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

n = 1 

while(n < 4):
    mes = int(input('Escolha um mes (1-12):'))
    if 1 <= mes <=12:
        print('É o mes de {}'.format(meses[mes-1]))
    n +=1

#meses.append >>> Adiciona dados a lista, somente um por vez
#meses.extend >>> Adiciona o dados + de um
#meses * 2   >>> multiplicar os dados da lista
# São mutaveis

lista = [0,1]
lista.extend([2, 3])
lista += [4,5]
lista += [6]
lista *= 3

print (lista)

for valor in lista:
    print(valor)