
periodo = 0 
total = 0

while(periodo <= 30):
    print('Periodo trabalhados (>>{})'.format(periodo))
    periodo +=1
    nh= float(input('Digite as horas trabalhadas :\n'))
    total += nh
else:
    print('Total de horas trabalhadas : \n', total)

