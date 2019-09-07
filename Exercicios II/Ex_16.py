
pe = float(input('Digite o valor do produto :\n'))

valor = 0
cp = 0

cp = int(input('Selecione a condicao de pagamento: \n'+ 
    '(1) a vista em dinheiro ou cheque \n' +
    '(2) a vista com cartao de credito \n' +
    '(3) 2x sem juros \n' + 
    '(4) 3x com acrescimo de 10% \n '))

while cp == 1:
    valor = pe - 0.10
    if (cp == 2):
        valor = pe -0.05
    elif (cp == 3):
        valor = pe /2
    elif (cp == 4):
        valor = pe + (pe * 10/100)

print ('Valor final = {}'.format(valor))