print('*** De tanque Cheio ***')

TC = input('Selecione o tipo de gasolina (G)gasolina (A)álcool:\n ')

CT = int(input("Digite a capacidade do tanque: \n"))

VG1 = CT * 1.80
VG2 = CT * 1

if (TC == G):
    print ('O valor ser gasto será :\n ', VG1)
elif(TC == A):
    print ('O valor gasto será :\n', VG2)