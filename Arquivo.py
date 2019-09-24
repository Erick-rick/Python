
#Abrir arquivo

arquivo = open('texto.txt','w')

#escrever conteudo no arquivo
arquivo.write('banana')
arquivo.write('pera')



#fechar arquivo
arquivo.close()

# modo 'a' de append
arquivo = open('texto.txt', 'a')

arquivo.write('morango\n')

arquivo.write('manga\n')

#ler arquivo
arquivo.read()

for linha in arquivo:
    print(linha)

arquivo = open('texto.txt', 'r')
palavra = []

for linha in arquivo:
    linha = linha.strip()
    palavra.append(linha)

arquivo.close()