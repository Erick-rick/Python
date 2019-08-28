print('*** Valores de vendas ***')

nome = input('Digite o nome do vendedor: \n')

vm = float (input('Digite o valor de vendas do mês do vendedor: \n'))

if (vm >=1000 and vm <= 5000):
    print('Parabens, {}!!  '.format(nome))
else:
    print('Lamento! Meta não alcançada!')