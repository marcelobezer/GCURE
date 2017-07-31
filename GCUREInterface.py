from Tkinter import *

class JanelaPrincipal (Frame):
    def __init__(self, master=None):
        def abrir(self): print "abrir"

        def salvar(self): print "salvar"

        def ajuda(self): print "ajuda"
        Frame.__init__(self, master)
        self.top=Tk()
        self.principal=Menu(self.top)
        self.arquivo=Menu(self.principal)
        self.arquivo.add_command(label="Abrir", command=abrir)
        self.arquivo.add_command(label="Salvar", command=salvar)
        self.principal.add_cascade(label="Arquivo", menu=self.arquivo)
        self.principal.add_command(label="Ajuda", command=ajuda)
        self.top.configure(menu=self.principal)



