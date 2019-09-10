#periodo = int (input('Digite o periodo trabalhado :'))
periodo = 1
#sal = 10
total = 0

while(periodo <= 3):
    print('Periodo trabalhados (>>{})'.format(periodo))
    periodo +=1
    nh= float(input('Digite as horas trabalhadas :\n'))
    total += nh
    sal = 10 * total
else:
    print('Total de horas trabalhadas : {}\n Salario ={}\n'.format(total, sal))
