texto = input('Digite uma palavra')

print('O tipo primitivo é ', type(texto))
print('Tem espaço?' , texto.isspace())
print('É um numero?', texto.isnumeric())
print('é Alfabetico?', texto.isalpha())
print('E alfanumerico',texto.isalnum())
print('Esta em maiuscula',texto.isupper())
print('Está em minisculas', texto.islower())
print('Está capitalizada?', texto.istitle())