numero = int(input('Fatorial de : \n'))

resultado =1 
cont = 1

while(cont <= numero):
    resultado *= cont
    cont += 1 

print('Resultado == : ', resultado)