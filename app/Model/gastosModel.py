from dataclasses import dataclass
from app.Model.categoriasModel import Categorias
from app.Model.databaseManager import DBTransactionManager, BaseDB
from app.Model.categoriasModel import CategoriasDB

@dataclass
class Gastos:
    data: str = None
    valor: float = None
    id: int = None
    categoria: Categorias = None

    def __post_init__(self):
        pass  # TODO adicionar validação dos campos


class GastosDB:

    def __init__(self):
        self._db = BaseDB()
        self._categoriaBD = CategoriasDB()

    def registrar_gasto_com_transacao(self, gasto: Gastos, categorias: Categorias, CPF):
        with DBTransactionManager():
            categoria_id = self._categoriaBD.vincular_categoria(categorias, CPF)
            self.registrar_gasto(categoria_id, gasto, CPF)

    def registrar_gasto(self, categoria, gasto, CPF):
        self._db.executar_transacao(
            comando="INSERT INTO Gastos (data, valor, categoria_id, usuario_id) VALUES (?, ?, ?, ?)",
            params=(gasto.data, gasto.valor, categoria, CPF),
        )
        return "Gasto inserido com sucesso!"
        

    def atualizar_gasto(self, categoria_nome, gasto: Gastos):

        with DBTransactionManager() as db_manager:
            db_manager.executar_transacao(
                comando="UPDATE Gastos SET data = ?, valor = ? WHERE id = ?",
                params=(gasto.data, gasto.valor, gasto.id),
            )

            db_manager.executar_transacao(
                comando="UPDATE Categorias SET nome = ? WHERE id = (SELECT categoria_id FROM Gastos WHERE id = ? LIMIT 1);",
                params=(categoria_nome, gasto.id),
            )
        return "Gasto atualizado com sucesso!"

    def listar_gastos(self, gastos: Gastos, CPF):
        with DBTransactionManager():
            if gastos.id is not None:
                resultado = self.recuperar_gasto(gastos.id, CPF)
            else:
                resultado = self.recuperar_gastos_registrados(CPF)

            if resultado:
                gastos = [
                    self.converter_consulta_de_gastos_em_objeto(row)
                    for row in resultado
                ]
                return gastos
            return []

    def recuperar_gasto(self, gasto_id: int, CPF):
        gasto = self._db.executar_transacao(
            
            comando="SELECT Gastos.id AS gasto_id, data, valor, Categorias.nome AS categoria_nome "
                "FROM Gastos " 
                "JOIN Categorias ON Gastos.categoria_id = Categorias.id " 
                "WHERE gasto_id = ? AND Gastos.usuario_id = ? ORDER BY data_insercao DESC",
            params=(gasto_id, CPF)
        )
        return gasto

    def recuperar_gastos_registrados(self, CPF):
        gastos = self._db.executar_transacao(
            comando="SELECT Gastos.id AS gasto_id, data, valor, Categorias.nome AS categoria_nome "
                "FROM Gastos " 
                "JOIN Categorias ON Gastos.categoria_id = Categorias.id " 
                "WHERE Gastos.usuario_id = ? ORDER BY data_insercao DESC",
            params=(CPF,)

        )
        return gastos

    def converter_consulta_de_gastos_em_objeto(self, consulta) -> Gastos:
        gasto = {
            "id": consulta[0],
            "data": consulta[1],
            "valor": consulta[2],
            "categoria_nome": consulta[3],
        }
        return gasto

    def listar_gasto_mes(self, mes, CPF):
        # Open a transaction to ensure the database connection is managed properly
        with DBTransactionManager() as db_manager:
            resultado = db_manager.executar_transacao(
                comando="SELECT * FROM Gastos "
                        "WHERE strftime('%m', data) = ? AND usuario_id = ?",
                        params=(mes, CPF)
            )
            if resultado:
                gastos = [
                    self.converter_consulta_de_gastos_em_objeto(row)
                    for row in resultado
                ]
                return gastos
            return []


    def deletar_gasto(self, gasto_id):
        with DBTransactionManager() as db_manager:
            db_manager.executar_transacao(
                comando="DELETE FROM Gastos WHERE id = ?",
                params=(gasto_id,),
            )
        return "Gasto deletado com sucesso!"


def converte_gasto_horas(gastos, ganho_por_hora):
    for gasto in gastos:
        gasto.valor = gasto.valor / ganho_por_hora
    return gastos