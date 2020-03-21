import pandas as pd

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv"

filmes = pd.read_csv(uri)
filmes.head()

filmes.columns = ('filmeId', 'titulo', 'generos')
filmes.head()

media =(1000 + 3000 + 3000 + 700000)/4
