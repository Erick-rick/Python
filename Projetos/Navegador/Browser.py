from gi.repository import Gtk, WebKit

class Brower(object):
    def __init__(self):

         # Obtendo os widgets do arquivo gerado pelo glade
        builder = Gtk.Builder()
        builder.add_from_file('BrowserPy')
        self.window = builder.get_object("window")
        self.window.show()
        self.go_back_button = builder.get_object('go_back')
        self.go_forward_button = builder.get_object('go_forward')
        self.refresh_button = builder.get_object('refresh')
        self.scrolledwindow = builder.get_object('scrolledwindows')
        self.url = builder.get_object('entry')
        self.search_entry = builder.get_object('search_entry')

        # Instanciando a classe do webkit que irá exibir a página
        self.view = WebKit.WebView()
        self.scrolledwindow.add(self.view)

        #Pagina inicial ao iniciar
        self.view.open('http://www.google.com.br')
        self.view.show()
        
        #Conectando os sinais do webkit
        self.view.connect(("load-committed", self.check_buttons) 
        self.view.connect("title-changed", self.change_title)

        #Conectando os sinais do Gtk
        builder.connect({"gtk_main_quit": Gtk.main.quit,
                         "on_entry_activate": self.go_, 
                         "on_search_activate": self.search, 
                         "go_back_clicked": self.go_back, 
                         "go_forward_clicked": self.go_forward,
                          "refresh_clicked": self.refresh})
    
    def go_(self, widget):
        #Carrega a página da barra de endereço
        link = self.url.get_context()
        if link.startswith('http://'):
            self.view.open(link)
        else:
            self.view.open('http://' + link)
        self.view.show()
    
    def search(self, widget):
        #Pesquisa no google o conteudo da barra de pesquisa
        text = self.search_entry.get_text()
        text = text.replace(" ", '+')
        self.url.set_text('http://www.google.com.br/search?q=' + text)
        self.search_entry.set_text("")
        self.go_(self)
    
    def check_buttons(self, widget, data):
        '''Verifica se os botões voltar, avançar estão disponíveis, em caso verdadeiro os botões podem ser utilizados caso contrário os botões são desativados.
           Também atualiza a barra de endereços com a página atualmente carregada'''
           uri = widget.get_main_frame().get_uri()
           self.url.set_text(uri)
           self.go_back_button.set_sensitive(self.view.can_go_forward())
           self.go_forward_button.set_sensitive(self.view.can_go_forward())

    def change_title(self, widget, data, arg):
        #Altera o título do navagador para titulo da pagina atualmente carregada
        title = widget.get_maion_frame().get_title()
        self.window.set_title('Py Brower - %s' %title)

    def go_back(self, widget):
        #Voltar página
        self.view.go_back()

    def go_forward(self, widget):
        #Avança a página
        self.view.go_forward()
    
    def refresh(self, wiget):
        #Atualizar página
        self.view.reload()

if __name__ =="__main__":
    brower = Brower()
    Gtk.main()