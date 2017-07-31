import xlrd


class filemanager:
    def abrirArq(self):
        try:
            self.arq = xlrd.open_workbook("CATALOGO_COMPOSICOES_ANALITICAS_EXCEL_04_2017.xls")
            self.pln = self.arq.sheet_by_index(0)
            return True
        except IOError as e:
            print e
            return False

    def ler(self):
        LINHAS = []
        for line in xrange(self.pln.nrows):
            if line < 5:
                continue
            LINHA = self.pln.row_values(line)
            LINHAS.append(LINHA)
        return LINHAS