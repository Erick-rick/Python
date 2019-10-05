# Range um tipo de sequencia imutavel de numeros, usado para
#looping de um numero espoecifico de vezes em um comando FOR 

sequencia = range (1, 5)

print(sequencia)

print('***************************************************')
#Range não imprime os elementos da sequencia, apenas armazena seu inicio e final
#Para imprimir seus elementos precisamos de um FOR:

for valor in range(1,5):
    print(valor)

print('***************************************************')
#O comando é a de poder controlar o passo da sequencia adicionado um terceiro parametro
# variando entre um numero e seu sucessor

for terceiro in range (1, 10 ,2):
    print(terceiro)

