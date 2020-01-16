import Tkinter import *
import math import *
import sys


class Calculator:
    def __init __(self, toplevel):

        #Janela
        toplevel.title('Calculadora')
        toplevel.geometry("210X200")

        #Espaçamento 
        self.frame1 = Frame1(toplevel)
        self.frame1.pack()

        #Box 1
        self.frame2 = Frame(toplevel)
        self.frame2.pack()

        #Box 2 
        self.frame3 = Frame(toplevel)
        self.frame3.pack()

        #Operações
        self.frame4 = Frame(toplevel, pady=12)
        self.frame4.pack()

        #Resultado
        self.frame5 = Frame(toplevel)
        self.frame5.pack()

        #Botoes
        self.frame6 = Frame(toplevel, pady= 12)
        self.frame6.pack()

        #Cor e tamanho das letras
        Label (self.frame1, txt= '' fg ='black', font= ('Verdana', '10'), height = 1).pack()
        
        #btn Somar
        somar=Button(self.frame4)