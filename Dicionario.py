# Dicionario*********************
# é estrutura de dados em Python e seus elementos como conjuntos 
# não são ordenados

pessoa = {'nome':'Ana', 'idade': 25, 'cidade': 'BH'}

print(pessoa)

pessoa ['nome']

#adicionar algum elemento
pessoa ['pais'] = 'Brasil'

print(pessoa)

#acessar seus elementos atraves de chaves(keys que o conjunto de chaves)

pessoa.keys()

#retorna seus valores

pessoa.values()

#Criar um dicionário
mylist = ["a", "b", "a", "c", "c"]
#Converter em uma lista
mylist = list( dict.fromkeys(mylist) )
#Imprimir a lista
print(mylist)

