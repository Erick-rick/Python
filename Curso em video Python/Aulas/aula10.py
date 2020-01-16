###Estrutura condicionais simples e composta

tempo = int(input('Quanto anos tem seu carro?'))

if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')

print('__FIM__')

#condição simplificada
print('novo' if tempo <=4 else 'velho')


nome= str(input('Qual é sei nome ?'))
if nome == 'Gustavo':
    print('Que nome voce tem')
else:
    print('Seu nome e diferente')
print('Bom dia,{}'.format(nome))


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m =(n1 + n2)/ 2
if m >6.0:
    print('Aprovado')
else:
    print('Reprovado!')
