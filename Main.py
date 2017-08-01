# -*- coding: utf-8 -*-
import BDManager
import FILEManager
import simplejson as json
import GCUREInterface
from Tkinter import *

def encontrarInsumo(S):
    LInsumo = BD.listaInsumo()
    S = S.upper()
    for i in xrange(len(LInsumo)):
        if LInsumo[i][1].find(S) != -1:
            print LInsumo[i]

def encontrarComposicao(S):
    LComposicao = BD.listaComposicao()
    S = S.upper()
    for i in xrange(len(LComposicao)):
        if LComposicao[i][1].find(S) != -1:
            print LComposicao[i]

def exibirComposicao(id):
    LComposicao = BD.lerComposicaoXComposicao(int(float(id)))
    LInsumo = BD.lerComposicaoXInsumo(int(float(id)))
    for i in xrange(len(LComposicao)):
        print BD.lerComposicao(int(float(LComposicao[i][1])))
    for i in xrange(len(LInsumo)):
        print BD.lerInsumo(int(float(LInsumo[i][1])))

def exibirInsumo(id):
    LInsumo = BD.lerInsumoXComposicao(int(float(id)))
    for i in xrange(len(LInsumo)):
        print BD.lerComposicao(int(float(LInsumo[i][0])))

if __name__=='__main__':
    BD = BDManager.BDManager()
    FM = FILEManager.filemanager()
    R = False
    if R:
        BD.resetarBanco()
        if FM.abrirArq() is True:
            AQV = FM.ler()
            CONT = 0
            for i in xrange(len(AQV)):
                if AQV[i][0] != "COMPOSICAO" and AQV[i][0] != "INSUMO":
                    T = AQV[i][1]
                    T = str(T).replace("/", "000")
                    T = int(float(T))
                    BD.inserirComposicao(int(T), json.dumps(AQV[i][2]).encode('utf-8'),
                                         json.dumps(AQV[i][3]).encode('utf-8'), float(0.0))
                else:
                    if AQV[i][0] == "INSUMO":
                        H = AQV[i][1]
                        H = str(H).replace("/", "000")
                        if BD.verficarInsumo(int(float(H))):
                            BD.inserirInsumo(int(float(H)), json.dumps(AQV[i][2]).encode('utf-8'),
                                             json.dumps(AQV[i][3]).encode('utf-8'), float(0.0))
                        BD.inserirComposicaoXInsumo(int(T), int(float(H)))
                    else:
                        H = AQV[i][1]
                        H = str(H).replace("/", "000")
                        BD.inserirComposicaoXComposicao(int(T), int(float(H)))


    #encontrarInsumo('VIBRADOR')
    #encontrarComposicao('Torque')
    #exibirComposicao(89264)
    #exibirInsumo(37731)

    root = Tk()
    app = GCUREInterface.JanelaPrincipal(master = root)
    GCUREInterface.mainloop()







