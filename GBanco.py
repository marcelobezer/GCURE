import sqlite3
import os.path

class GBanco:
    def __init__(self):
        self.check = os.path.isfile('BancoDados.bd')
        self.conn = sqlite3.connect('BancoDados.bd')
        self.conn.text_factory = str
        self.cur = self.conn.cursor()
        if not self.check:
            self.gerarBanco()

    def __del__(self):
        self.conn.close()

    def gerarBanco (self):
        #Criar tabela de composicoes
        self.conn.execute("""
        CREATE TABLE composicoes (
          id INTEGER NOT NULL PRIMARY KEY,
          descricao TEXT NOT NULL,
          unidade TEXT NOT NULL,
          preco REAL NOT NULL
        );
        """)

        #Criar tabela de insumos
        self.conn.execute("""
        CREATE TABLE insumos (
          id INTEGER NOT NULL PRIMARY KEY,
          descricao TEXT NOT NULL,
          unidade TEXT NOT NULL,
          preco REAL NOT NULL
        );
        """)

        #Criar tabela de insumos nas composicoes
        self.conn.execute("""
        CREATE TABLE composicoesXinsumos (
          idComposicao INTEGER NOT NULL,
          idInsumo INTEGER NOT NULL
        );
        """)

        #Criar tabela de composicoes em composicoes
        self.conn.execute("""
        CREATE TABLE composicoesXcomposicoes (
          idComposicao INTEGER NOT NULL,
          idComposicaoInterna INTEGER NOT NULL
        );
        """)



