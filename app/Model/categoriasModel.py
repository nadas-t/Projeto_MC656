from dataclasses import dataclass
from app.Model.databaseManager import DBTransactionManager, BaseDB


@dataclass
class Categorias:
    id: int = None
    nome: str = None

    def __post_init__(self):
        pass


class CategoriasDB:
    def __init__(self):
        self._db = BaseDB()

    def adicionar_categoria(self, categoria: Categorias):
        with DBTransactionManager() as db_manager:
            db_manager.executar_transacao(
                comando="INSERT INTO Categorias (nome) VALUES (?)",
                params=(categoria.nome,),
            )
        return "Categoria adicionada com sucesso!"

    def listar_categorias():
        with DBTransactionManager() as db_manager:
            resultado = db_manager.executar_transacao(
                comando="SELECT * FROM Categorias",
                fetchall=True,
            )
            if resultado:
                Categorias = [
                    {
                        "id": row[0],
                        "data": row[1],
                        "valor": row[2],
                        "categoria_nome": row[3],
                    }
                    for row in resultado
                ]
                return Categorias
        return []

    def atualizar_categoria(self, categoria: Categorias):
        with DBTransactionManager() as db_manager:
            db_manager.executar_transacao(
                comando="UPDATE Categorias SET nome = ? WHERE id = ?",
                params=(categoria.nome, categoria.id),
            )
        return "Categoria atualizada com sucesso!"

    def deletar_categoria(self, categoria: Categorias):
        with DBTransactionManager() as db_manager:
            db_manager.executar_transacao(
                comando="DELETE FROM Categorias WHERE id = ?",
                params=(categoria.id,),
            )
        return "Categoria deletada com sucesso!"
