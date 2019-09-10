num = 0 
maior = 0 
menor = 0

num = int (input('Digite um numero: \n'))

for n in num(1, 20):
    if (n == 0):
        maior = num
        menor = num
    elif(num > maior):
        maior = num
    elif(num < menor):
        menor = num

print('Maior = {}\n Menor = {} '.format(maior, menor))