

horaTrabalhada = int(input('Digite as Horas trabalhas :\n'))
valorHora = int(input('Valor da Hora:'))

sal_Bruto = horaTrabalhada * valorHora

INSS = sal_Bruto/100 * 11

if (sal_Bruto > 1257 and sal_Bruto <= 2512):
    IR = sal_Bruto/100 * 15
elif( sal_Bruto > 2512):
    IR = sal_Bruto/100 * 27.5

sal_liquido = sal_Bruto - INSS - IR

print ('Valor INSS: {} \n Valor do IR : {} \n Salario liquido : {}'.format(INSS, IR, sal_liquido))

