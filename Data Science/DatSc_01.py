import pandas as pd   #apelido para pandas >> pd

uri = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv'
filmes = pd.read_csv(uri) # Data Frame
filmes.head() # head mostra 5 elementos


#alteração dos titulos das colunas
filmes.columns = ["filmesId", "titulo", "generos"]
filmes.head()

#notas----------------------------------------------------------------------------------
notas = pd.read_csv(uri)
notas.head()

notas.columns['usuárioId', 'filmeId', 'nota', 'momento']
notas.head()

# somente a coluna notas
notas['notas'].head() #series

#variação de notas
notas['notas'].unique()

#Media de notas
notas['notas'].mean()

#Nota minima
notas['notas'].min()

#descrever todas colunas
#com varias medidas estaticas basicas
notas.describe()

#media
media = (1 + 3 + 3 +7 )/ 4
print (media)
#media (1000 + 3000 + 3000 + 700000)/4

#mediana 
#divide 50% esq / 50%dir
