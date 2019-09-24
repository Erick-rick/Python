import numpy 

lista = [1, 2, 3, 4, 5]

x = numpy.array(lista)
print(x)

#array fornece faciidade para realizar operações matemáticas com escalares

z = numpy.array ([1, 2, 3, 4, 5, 6])
y = 2

print(x + y)
print(x - y)
print(y - x)
print(x * y)
print(x / y)
print(y / x)
print('*****************************************')

a = numpy.array([1, 2, 3, 4, 5])
b = numpy.array([6, 7, 8, 9, 10])

print(x + y)
print(x - y)
print(y - x)
print(x * y)

numpy.sum(a) #soma todos os elementos de a
numpy.max(a) #retorna o valor maximo contido em a 
numpy.min(a) #retorna o valor minimo contido em a
