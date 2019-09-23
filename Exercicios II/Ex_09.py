print('***calculo de salario')

sal = float(input('Digite o salario do funcionario: '))
sal_novo = 0

if (sal <= 500):
    sal_novo = sal * 0.15
elif(sal >= 500 and sal<= 1000):
    sal_novo = sal * 0.10
elif(sal > 1000):
    sal_novo = sal * 0.05

print('O novo salario é {}'.format(sal_novo))
