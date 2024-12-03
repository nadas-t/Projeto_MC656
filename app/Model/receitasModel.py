from dataclasses import dataclass
from app.Model.categoriasModel import Categorias
from app.Model.databaseManager import DBTransactionManager, BaseDB
from app.Model.categoriasModel import CategoriasDB


@dataclass
class Receitas:
    data: str = None
    valor: float = None
    id: int = None
    categoria: Categorias = None

    def __post_init__(self):
        pass  # TODO adicionar validação dos campos

class ReceitasDB:

    def __init__(self):
        self._db = BaseDB()
        self._categoriaBD = CategoriasDB()

    def registrar_receita_com_transacao(self, receita: Receitas, categorias: Categorias, CPF):
        with DBTransactionManager():
            categoria_id = self._categoriaBD.vincular_categoria(categorias, CPF)
            self.registrar_receita(categoria_id, receita, CPF)

    def registrar_receita(self, categoria, receita, CPF):
        self._db.executar_transacao(
            comando="INSERT INTO Receitas (data, valor, categoria_id, usuario_id) VALUES (?, ?, ?, ?)",
            params=(receita.data, receita.valor, categoria, CPF),
        )
        
        return "Receita cadastrada com sucesso!"

    def atualizar_receita(self, categoria_nome, receita: Receitas):
        with DBTransactionManager() as db_manager:
            db_manager.executar_transacao(
                comando="UPDATE Receitas SET data = ?, valor = ? WHERE id = ?",
                params=(receita.data, receita.valor, receita.id),
            )

            db_manager.executar_transacao(
                comando="UPDATE Categorias SET nome = ? WHERE id = (SELECT categoria_id FROM Receitas WHERE id = ? LIMIT 1);",
                params=(categoria_nome, receita.id),
            )

        return "Receita atualizada com sucesso!"

    def listar_receitas(self, receitas: Receitas, CPF):
        with DBTransactionManager():
            if receitas.id is not None:
                resultado = self.recuperar_receita(receitas.id, CPF)
            else:
                resultado = self.recuperar_receitas_registradas(CPF)
            if resultado:
                receitas = [
                    self.converter_consulta_de_receitas_em_objeto(row)
                    for row in resultado
                ]
                return receitas
            return []

    def recuperar_receita(self, receita_id: int, CPF):
        receita = self._db.executar_transacao(
            
            comando="SELECT Receitas.id AS receita_id, data, valor, Categorias.nome AS categoria_nome "
                "FROM Receitas " 
                "JOIN Categorias ON Receitas.categoria_id = Categorias.id " 
                "WHERE receita_id = ? AND Receitas.usuario_id = ? ORDER BY data_insercao DESC",
            params=(receita_id, CPF)
        )
        return receita

    def recuperar_receitas_registradas(self, CPF):
        receitas = self._db.executar_transacao(
            comando="SELECT Receitas.id AS gasto_id, data, valor, Categorias.nome AS categoria_nome "
                "FROM Receitas " 
                "JOIN Categorias ON Receitas.categoria_id = Categorias.id "  
                "WHERE Receitas.usuario_id = ? ORDER BY data_insercao DESC",
            params=(CPF,)
        )
        return receitas

    def converter_consulta_de_receitas_em_objeto(self, consulta) -> Receitas:
        receita = {
            "id": consulta[0],
            "data": consulta[1],
            "valor": consulta[2],
            "categoria_nome": consulta[3],
        }
        return receita

    def deletar_receita(self, receita_id):
        with DBTransactionManager() as db_manager:
            db_manager.executar_transacao(
                comando="DELETE FROM Receitas WHERE id = ?",
                params=(receita_id,),
            )
        return "Receita deletada com sucesso!"


def converte_receita_horas(receitas, receita_por_hora):
    for receita in receitas:
        receita.valor = receita.valor / receita_por_hora
    return receitas