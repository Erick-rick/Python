class Conta:
    def __init__ (self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    
    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append('Depósito de {}'.format(valor))
        print('Valor depositado com sucesso!')


    def sacar(self, valor):
        if(self.valor < valor):
            return False
            print('>>Saldo Indisponivel!!')
        else:
            self.saldo -=valor
            self.historico.transacoes.append('Saque de {}'.format(valor))
            return True

    def transferir(self, destino ,valor):
        #self.valor -= valor
        #destino.saldo += valor
        retirou = self.sacar(valor)
        if(retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append('Transferencia de {} para conta {}'.format(valor, destino.numero))
            return True

    def extrato(self):
        print('Titula :{} \n numero:{} \n >>>Saldo:{}'.format(self.titular, self.numero, self.saldo))
        self.historico.transacoes.append('Extrato retirado > Saldo de {}'.format(self.saldo))