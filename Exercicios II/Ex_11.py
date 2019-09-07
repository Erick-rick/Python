print ('***Codigo de livros****')

CL = input('Digite o codigo do livro : (A / B)')


if (CL == 'A'and CL =='a') :
    print('Livro de ficcao')
elif (CL == 'B' and CL == 'b'):
    print('Livro de nao-ficcao')
elif (CL != 'A' and CL != 'B'):
    print('Codigo invalido')

