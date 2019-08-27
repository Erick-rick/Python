print ('*** Peso ideal ***')

H = float (input('Digite a sua altura :\n'))

S = input('Qual é o seu sexo : M-masculino F-Feminino')

Pm = (72,7 * H) - 58   # peso ideal masculino
Pf = (62,1 * H) - 44,7 # peso ideal feminino

if (S == m or S == M):
    print( 'Seu peso ideal é ', Pm)
elif(S == f or S == F ):
    print('Seu peso ideal é  ', Pf)
