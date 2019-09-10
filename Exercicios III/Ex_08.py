
num = 0 
maior = 0 
menor = 0

num = int (input('Digite um numero: \n'))

for n in num:
    if (n == 0):
        maior = num
        menor = num
    elif(num > maior):
        maior = num

print('Maior = ', maior)

    
