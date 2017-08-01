# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
import webbrowser
import os


class JanelaPrincipal (Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.criarMenu(master)
        self.master.title("GCURE")
        self.master.geometry("720x600+100+100")

    def erro(self, e):
        tkMessageBox.showinfo("Erro", e)

    def hello(self):
        print "Hello"

    def sobre(self):
        tkMessageBox.showinfo("Versão", str("Versão: 1.0\n\nInstituto Federal de Ciência, Educação e\n"
                                             "Tecnologia do Ceará, Campus Crato\n\nLaIS - 2017\n\n"
                                             "github.com/marcelobezer/GCURE"))

    def abrirAjuda(self):
        if os.path.isfile('GCURE.pdf'):
            webbrowser.open_new(r'GCURE.pdf')
        else:
            self.erro("Não foi possivel abrir o arquivo de ajuda")

    def criarMenu(self, root):
        menubar = Menu(root)

        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Arquivo", menu=filemenu)
        filemenu.add_command(label="Abrir(.xls)", command=self.hello)
        filemenu.add_separator()
        filemenu.add_command(label="Sair", command=root.quit)

        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ajuda", menu=helpmenu)
        helpmenu.add_command(label="Guia de uso", command=self.abrirAjuda)
        helpmenu.add_separator()
        helpmenu.add_command(label="Sobre", command=self.sobre)

        root.config(menu=menubar)





