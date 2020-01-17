import pandas
from sklearn import linear_model

#O módulo Pandas nos permite ler arquivos csv e retornar um objeto DataFrame.
df = pandas.read_csv("cars.csv")

# Em seguida, faça uma lista dos valores independentes e chame essa variável X.
# Coloque os valores dependentes em uma variável chamada y.
X = df[['Weight', 'Volume']]
y = df['CO2']

#No módulo sklearn, usaremos o LinearRegression()método para criar um objeto de regressão linear.
#Este objeto possui um método chamado fit()que usa os valores independentes e dependentes como parâmetros e preenche o objeto de regressão com dados que descrevem o relacionamento
regr = linear_model.LinearRegression()
regr.fit(X, y)

#temos um objeto de regressão pronto para prever valores de CO2 com base no peso e no volume de um carro
#predict the CO2 emission of a car where the weight is 2300g, and the volume is 1300ccm:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)