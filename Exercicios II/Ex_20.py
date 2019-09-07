

a = float(input('Digite o comprimento do lado A:\n'))
b = float(input('Digite o comprimento do lado B: \n'))
c = float(input('Digite o comprimento do lado C: \n'))

if (a == b and b == c):
    print('>>>>>> Equilatero!')
elif(a == b or b == c):
    print('>>>>> Isosceles')
elif(a!= b and b!= c and a!= c):
    print('>>>>> Escaleno')