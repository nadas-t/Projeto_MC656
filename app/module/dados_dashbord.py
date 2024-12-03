from app.Model.databaseManager import DBTransactionManager, BaseDB
from datetime import datetime

from app.Model.gastosModel import (
    GastosDB,
    Gastos,
)

from app.Model.receitasModel import (
    ReceitasDB,
    Receitas,
)

class Dashboard:

    def __init__(self):
        self._db = BaseDB()

    def saldo(self, CPF):
        saldo = 0

        gasto = Gastos(id=None)
        gasto_db = GastosDB()
        gastos = gasto_db.listar_gastos(gasto, CPF)

        receita = Receitas(id=None)
        receita_db = ReceitasDB()
        receitas = receita_db.listar_receitas(receita, CPF)

        if receitas and len(receitas) > 0:
            for receita in receitas:
                saldo = saldo + receita['valor']

        if gastos and len(gastos) > 0:
            for gasto in gastos:
                saldo = saldo - gasto['valor']

        return saldo

    def movimentacoes(self, CPF):
        # Open a transaction to ensure the database connection is managed properly
        with DBTransactionManager() as db_manager:
            movimentacoes = db_manager.executar_transacao(
                comando="SELECT g.data, g.valor, c.nome AS categoria_nome, g.tipo "
                        "FROM (SELECT data, valor, categoria_id, data_insercao, 'Gasto' AS tipo, usuario_id "
                        "FROM Gastos WHERE usuario_id = ? "
                        "UNION ALL "
                        "SELECT data, valor, categoria_id, data_insercao, 'Receita' AS tipo, usuario_id "
                        "FROM Receitas WHERE usuario_id = ? "
                        ") AS g "
                        "JOIN categorias AS c ON g.categoria_id = c.id ORDER BY g.data_insercao DESC LIMIT 20;",
                        params=(CPF, CPF),
                )

            dados = [self.converter_consulta_de_movimentacoes_em_objeto(row) for row in movimentacoes]
            
            return dados

    def converter_consulta_de_movimentacoes_em_objeto(self, consulta) -> dict:
        return {
            "data": consulta[0],
            "valor": consulta[1],
            "categoria": consulta[2],
            "tipo": consulta[3],
        }
        
    def gastos_mes(self, CPF):

        valor = 0
        data_atual = datetime.now()
        mes_atual = data_atual.strftime('%m')  # '%m' retorna o mês com 2 dígitos

        gasto = Gastos(id=None)
        gasto_db = GastosDB()
        gastos = gasto_db.listar_gasto_mes(mes_atual, CPF)

        if gastos and len(gastos) > 0:
            for gasto in gastos:
                valor = valor + gasto['valor']
        
        return valor