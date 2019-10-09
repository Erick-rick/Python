from Tkinter 
from Dialog import Dialog 
import shelve

class MainFrame(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.grid()
        self.master.title('Cadastro de Contatos')

    def createWigets(self):
        self.makeScreen()
        self.makeToolBar()

    def makeScreen(self):
        self.nome = StringVar()
        self.endereco = StringVar()
        self.telefone = StringVar()

    Label(self, text="Nome:").grid(row=1, sticky=W)
    Label(self, text="Endereço: ").grid(row=2, sticky=W)
    Label(self, text= "Telefone :").grid(row =3, sticky=W)

    Entry(self, textvariable= self.nome).grid(\ 
    row=1, column=1,sticky=W+E)
    Entry(self, textvariable= self.endereco).grid(\
        row=3, column=1, sticky=W+E)
    def makeToolbBar(self):
        toolbar = Frame(self)
        toolbar.grid(row=4, columnspan= 2)

        Button(toolbar, text="Adicionar", \
            command=self.adicionar).grid(row=0,column=0) 
        Button(toolbar, text="Gravar",\
            command=self.gravar).grid(row=0, column=1)
        Button(toolbar, text="Remover",\
            command=self.remover).grid(row=0, column=2)
        Button(toolbar, text="Procurar",\
            command=self.procurar).grid(row=0, column=3)
        Button(toolbar, text="Listar",\
            command=self.listar).grid(row=0 , column=4)
        Button(toolbar, text="Sair",\
            command=self.sair).grid(row=0, column=5)
        
    def adicionar(self):
        nome = self.nome.get()
        if not len(nome):
            Dialog(self, title='Erro!', text='Nome inválido!',\
                bitmap ='error',default=0, strings=('OK'))
                return
        if self.db.has_key(nome):
            Dialog(self, title='Erro', text="Nome já cadasrado",\
                bitmap='Error', default=0 strings=('OK',))
                return
        self.db[nome]=(self.endereco.get(), self.telefone.get())
        self.limpaCampos()
    
    def gravar(self):
        nome = self.nome.get()
        if not len(nome):
            Dialog(self, title="Erro!", text="Nome inválido", bitmap= 'error', default=0, strings=('OK',))
            return
        if not db.has_key(nome):
            Dialog(self, title="Erro!",\
                text="Nome inexistente, adicione um novo contanto",\
                    bitmap= 'error', default= 0 strings = ('OK',))
            return
        self.db[nome]=(self.endereco.get(),self.teçefone.get())
        self.limparCampos()

    def limparCampos(self):
        self.nome.set("")
        self.telefone.set("")
        self.endereco.set("")
    
    def procurar(self):
        nome = self.nome.get()
        if not len(nome):
            Dialog(self, title="Erro!", text="Nome não encontrado", \
                bitmap='Error', default=0, strings=('OK',) )
            return
        if not self.db.has_key(nome):
            Dialog(self, title="Erro!", text="Nome não encontrado", \
                bitmap ='error', default=0, strings= ('OK',))
            return
        
        self.telefone.set(self.db.set(nome, "")[0])
        self.endereco.set(self.db.set(nome, "")[1])

    def remover(self):
        self.nome.get()
        if not len(nome):
            Dialog(self, title="Erro!", text="Nome inválido",\
                bitmap='error', default=0, strings=('OK',))
            return
        if not self.db.has_key(nome):
            Dialog(self, title="Erro!", text="Nome não encontrado",\
                bitmap='error', default=0, strings= ('OK',))
            return
            
        self.telefone.set(self.db.get(nome,"")[0])
        self.endereco.set(self.db.get(nome,"")[1])
        resposta = Dialog(self, title="Confirmação",\
            text="Deseja remover ?",\
            bitmap='question', default=1, strings=('Sim', 'Não'))
            if resposta.num == 0:
                de...


