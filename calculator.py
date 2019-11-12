import sys

class Valor:
    a = 0.000
    b = 0.000
    c = 0.000

    def valor1(self):
        try :
            self.a= input('Primeiro Valor: ')
            a = self.a 
            return a 
        except:
            print('Inválido, digite um número! Se for real digite . e não ,')
            self.valor1()
    
    def valor2(self):
        try:
            self.b = input('Segundo valor: ')
            b = self.b
            return b
        except:
            print('Inválido, digite um número! Se for real digite . e não ,')
            self.valor2()

class Operator:

    def somar(self, a, b):
        self.x = a + b
        x = self.x
        return x
    
    def subtrair(self, a, b):
        self.x = a - b
        x = self.x
        return x
    
    def multiplicar(self, a, b):
        self.x = a * b
        x = self.x
        return x
    
    def dividir(self, a, b):
        self.x = a / b
        x = self.x
        return x

class Resultado:

    def resultado(self, a, b, c):
        print('Resultado: %f')%(c)

if __name__=="__main__":

    p1 = Valor()
    v1 = p1.valor1()
    v2 = p2.valor2()

    p2 = Operator()

    p3 = Resultado()

    operacao = raw_input('Operação : (+) (-) (*) (/) ou (s)sair] :')

    while operacao:

        if operacao == 's':
            sys.exit()

        if operacao == '+':
            n1 = p2.somar(v1,v2)
            p3.resultado(None, None, n1)
        
        if operacao == '-':
            n1 = p2.subtrair(v1, v2)
            p3.resultado (None, None, n1)
        
        if operacao == '*':
            n1 = p2.multiplicar(v1, v2)
            p3.resultado(None, None, n1)
        
        if operacao == '/':
            n1 = p2.dividir(v1, v2)
            p3.resultado(None, None, n1)
        
        break



            