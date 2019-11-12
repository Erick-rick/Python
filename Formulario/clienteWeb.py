import os, sys

sys.path.append(os.path.dirname(__file__))

from cliente import *

def Inicializa(id, nome, end, bairro, tel):
    cliente(Nome == nome, Endereco - end, Bairro =bairro, telefone= tel)
    return 'Cadastrado'