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

<<<<<<< HEAD
=======
from app.Model.categoriasModel import (
    CategoriasDB,
    resgatar_nome_categoria,
)

>>>>>>> b83dd7e8 (implementa preenchimeto do grafico de gastos por categoria com dados do banco)
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
        data_atual = datetime.now()
        mes_atual = data_atual.strftime('%m')  # '%m' retorna o mês com 2 dígitos
        gasto_db = GastosDB()
        gastos = gasto_db.listar_gasto_mes(mes_atual, CPF)
        
        return gastos
    
    def calcular_gastos_por_categoria(self, CPF):
        valor_gasto_por_categoria = {}
        for gasto in self.gastos_mes(CPF):
            categoria = resgatar_nome_categoria(gasto['categoria_nome'])
            valor = gasto['valor']

            if categoria in valor_gasto_por_categoria:
                valor_gasto_por_categoria[categoria] += valor
            else:
                valor_gasto_por_categoria[categoria] = valor
        return valor_gasto_por_categoria
        