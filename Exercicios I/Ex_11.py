
ct = int(input('Digite o comprimento do tijolo:'))
lt = int(input('Digite a largura do tijolo:'))

cp = int(input('Digite o comprimento da parede:'))
lp = int(input('Digite o largura da parede:'))

qtd = (cp/ ct)* (lp/ lt)

print ('Sera necessario {} tijolos'.format(qtd))


### |__|__|__|   
#   |__|__|__|
#   |__|__|__|      tijolo 1x1 /parede 3x3