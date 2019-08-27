print ('***Quadro de funcionários***')

func = 0
 
while func < 4:

    NF = input('Digite o nome do funcionário:\n')
    Sal = float(input('Digite o salário do funcionário: \n'))
    DEP = input('Selecione o departamento do funcionário\n (P) - Produção \n (E) - Engenharia')
    func +=1

if (Sal >= 1000 and Sal <= 1500):
    print ('Funcionário : {} \n Departamento : {} \n Salário: \n'.format(NF, DEP, Sal))

