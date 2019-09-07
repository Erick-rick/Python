
cp = 0
classificacao = null

cp = int(input('Digite o codigo do produto:\n'))

if (cp == 1):
    classificacao = 'Alimento nao perecivel'
elif(cp >=2 and cp <=4):
    classificacao = 'Alimento perecivel'
elif(cp == 5 or cp ==6):
    classificacao = 'Vestuario'
elif(cp == 7 ):
    classificacao = 'Higiene pessoal'
elif(cp == 8 or cp == 9):
    classificacao = 'Limpeza e utensilios domesticos'
elif(cp != 0 and cp > 9 ):
    classificacao = 'codigo invalido!'

print( 'Classificado como >>> ')