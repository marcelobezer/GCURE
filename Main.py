import BDManager
import FILEManager
import simplejson as json
import GCUREInterface

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
    app = GCUREInterface.JanelaPrincipal()
    app.master.title("GCURE")
    app.master.geometry("720x600+100+100")
    GCUREInterface.mainloop()







