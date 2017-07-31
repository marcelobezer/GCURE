import GBanco

BD = GBanco.GBanco()
BD.conn.execute("PRAGMA synchronous = OFF")
BD.conn.execute("BEGIN TRANSACTION")

class BDManager:
    def inserirInsumo(self, id, descricao, unidade, preco):
        if type(id) == int and type(descricao) == str and type(unidade) == str and type(preco) == float:
            try:
                BD.conn.execute("""
                INSERT INTO insumos (id, descricao, unidade, preco)
                VALUES (?, ?, ?, ?)
                """, (id, descricao, unidade, preco))
                BD.conn.commit()
                return True
            except ValueError as e:
                print e
                return False
        return False

    def inserirComposicao(self, id, descricao, unidade, preco):
        if type(id) == int and type(descricao) == str and type(unidade) == str and type(preco) == float:
            try:
                BD.conn.execute("""
                INSERT INTO composicoes (id, descricao, unidade, preco)
                VALUES (?, ?, ?, ?)
                """, (id, descricao, unidade, preco))
                BD.conn.commit()
                return True
            except ValueError as e:
                print e
                return False
        return False

    def inserirComposicaoXComposicao(self, idComposicao, idComposicaoInterna):
        if type(idComposicao) == int and type(idComposicaoInterna) == int:
            try:
                BD.conn.execute("""
                INSERT INTO composicoesXcomposicoes (idComposicao, idComposicaoInterna)
                VALUES (?, ?)
                """, (idComposicao, idComposicaoInterna))
                BD.conn.commit()
                return True
            except ValueError as e:
                print e
                return False
        print "Tipos erro"
        return False


    def inserirComposicaoXInsumo(self, idComposicao, idInsumo):
        if type(idComposicao) == int and type(idInsumo) == int:
            try:
                BD.conn.execute("""
                INSERT INTO composicoesXinsumos (idComposicao, idInsumo)
                VALUES (?, ?)
                """, (idComposicao, idInsumo))
                BD.conn.commit()
                return True
            except ValueError as e:
                print e
                return False
        print "Tipos erro"
        return False

    def resetarBanco(self):
        try:
            BD.conn.execute("DELETE FROM composicoes")
            BD.conn.execute("DELETE FROM insumos")
            BD.conn.execute("DELETE FROM composicoesXinsumos")
            BD.conn.execute("DELETE FROM composicoesXcomposicoes")
            BD.conn.commit()
            return True
        except ValueError as e:
            print e
            return False

    def lerComposicao(self, id):
        if type(id) == int:
            try:
                BD.cur.execute("""
                SELECT * FROM composicoes
                WHERE id = ?
                """, (id,))
                valor = BD.cur.fetchone()
                return valor
            except ValueError as e:
                print e
                return False
        return False

    def lerInsumo(self, id):
        if type(id) == int:
            try:
                BD.cur.execute("""
                SELECT * FROM insumo
                WHERE id = ?
                """, (id,))
                valor = BD.cur.fetchall()
                return valor
            except ValueError as e:
                print e
                return False
        return False

    def lerComposicaoXInsumo(self, id):
        if type(id) == int:
            try:
                BD.cur.execute("""
                SELECT * FROM composicoesXinsumos
                WHERE idComposicao = ?
                """, (id,))
                valor = BD.cur.fetchall()
                return valor
            except ValueError as e:
                print e
                return False
        return False

    def lerComposicaoXComposicao(self, id):
        if type(id) == int:
            try:
                BD.cur.execute("""
                SELECT * FROM composicoesXcomposicoes
                WHERE idComposicao = ?
                """, (id,))
                valor = BD.cur.fetchall()
                return valor
            except ValueError as e:
                print e
                return False
        return False

    def verficarComposicao(self, id):
        if type(id) == int:
            try:
                BD.cur.execute("""
                SELECT * FROM composicoes
                WHERE id = ?
                """, (id,))
                valor = BD.cur.fetchall()
                if valor == None:
                    return True
                else:
                    return False
            except ValueError as e:
                print e
                return False
        return False

    def verficarInsumo(self, id):
        if type(id) == int:
            try:
                BD.cur.execute("""
                SELECT * FROM insumos
                WHERE id = ?
                """, (id,))
                valor = BD.cur.fetchall()
                if valor == []:
                    return True
                else:
                    return False
            except ValueError as e:
                print e
                return False
        return False