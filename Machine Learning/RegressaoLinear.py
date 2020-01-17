#A regressão linear usa a relação entre os pontos de dados para desenhar uma linha reta em todos eles.

#Importe os módulos necessários:
import matplotlib.pyplot as plt
from scipy import stats

#Crie as matrizes que representam os valores dos eixos x e y:
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#Execute um método que retorne alguns valores-chave importantes da regressão linear:
slope, intercept, r, p, std_err = stats.linregress(x, y)

#Crie uma função que use os valores slope e intercept para retornar um novo valor. 
# Este novo valor representa onde, no eixo y, o valor x correspondente será colocado:
def myfunc(x):
  return slope * x + intercept

#Execute cada valor da matriz x através da função Isso resultará em uma nova matriz 
# com novos valores para o eixo y:
mymodel = list(map(myfunc, x))

#Desenhe o gráfico de dispersão original:
plt.scatter(x, y)

#Desenhe a linha de regressão linear:
plt.plot(x, mymodel)

#Exiba o diagrama:
plt.show()

#>>>>>>>>>>PREVER VALORES FUTUROS<<<<<<<<<<<<<<<<<<<

from scipy import stats

a = [5,7,8,7,2,17,2,9,4,11,12,9,6]
b = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(a, b)

def myfunc1(x):
  return slope * x + intercept

speed1 = myfunc1(10)

print(speed1)


