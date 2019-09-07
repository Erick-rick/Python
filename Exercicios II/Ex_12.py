print('***Temperatura ****\n')


temp = float(input('Digite a temperatura ::\n'))

if (temp < 100):
    print('{} º A temperatura esta muito baixa! '.format(temp))
elif(temp >= 100 and temp <= 200):
    print('{} º A temperatura está normal!'.format(temp))
elif(temp > 200 and temp < 500):
    print('{}º A temperatura esta alta'.format(temp))
    