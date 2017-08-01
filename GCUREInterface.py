from Tkinter import *

class JanelaPrincipal (Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.criarMenu(master)
        self.master.title("GCURE")
        self.master.geometry("720x600+100+100")

    def hello(self):
        print "Hello"

    def criarMenu(self, root):
        menubar = Menu(root)

        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Arquivo", menu=filemenu)
        filemenu.add_command(label="Abrir (.xls)", command=self.hello)
        filemenu.add_separator()
        filemenu.add_command(label="Sair", command=root.quit)

        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ajuda", menu=helpmenu)
        helpmenu.add_command(label="Guia de uso", command=self.hello)
        helpmenu.add_separator()
        helpmenu.add_command(label="Sobre", command=self.hello)

        root.config(menu=menubar)





