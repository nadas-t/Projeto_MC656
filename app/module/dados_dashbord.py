from dataclasses import dataclass
from app.Model.databaseManager import DBTransactionManager, BaseDB

from app.Model.gastosModel import (
    GastosDB,
    Gastos,
)

from app.Model.receitasModel import (
    ReceitasDB,
    Receitas,
)

from app.Model.categoriasModel import (
    CategoriasDB,
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
                        "FROM (SELECT data, valor, categoria_id, data_insercao, 'Gasto' AS tipo " 
                        "FROM Gastos "
                        "UNION ALL "
                        "SELECT data, valor, categoria_id, data_insercao, 'Receita' AS tipo "
                        "FROM Receitas) AS g JOIN categorias AS c ON g.categoria_id = c.id "
                        "ORDER BY g.data_insercao DESC LIMIT 20",
            )

            receitas_objetos = [self.converter_consulta_de_receitas_em_objeto(row) for row in movimentacoes]
            return receitas_objetos

    def converter_consulta_de_receitas_em_objeto(self, consulta) -> dict:
        return {
            "data": consulta[0],
            "valor": consulta[1],
            "categoia": consulta[2],
            "tipo": consulta[3],
        }