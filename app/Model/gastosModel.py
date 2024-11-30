from dataclasses import dataclass
from app.Model.databaseManager import DBTransactionManager, BaseDB


@dataclass
class Gastos:
    id: int = None
    data: str = None
    valor: float = None
    categoria: int = None

    def __post_init__(self):
        pass


@dataclass
class Categorias:
    id: int = None
    nome: str = None

    def __post_init__(self):
        pass


class GastosDB:

    def __init__(self):
        self._db = BaseDB()

    def adicionar_gasto(self, gasto: Gastos, categorias: Categorias):
        try:
            with DBTransactionManager() as db_manager:
                # Verificar se a categoria já existe
                categoria = db_manager.executar_transacao(
                    comando="SELECT id FROM Categorias WHERE nome = ?",
                    params=(categorias.nome,),
                    fetchone=True,
                )

                # Se a categoria não existir, criar e recuperar o ID
                if categoria is None:
                    db_manager.executar_transacao(
                        comando="INSERT INTO Categorias (nome) VALUES (?)",
                        params=(categorias.nome,),
                    )
                    # Recuperar o último ID inserido
                    categoria_id = db_manager.executar_transacao(
                        comando="SELECT last_insert_rowid()",
                        fetchone=True,
                    )[0]
                else:
                    # Categoria já existente, pegar o ID
                    categoria_id = categoria[0]

                # Inserir o gasto com o ID da categoria
                db_manager.executar_transacao(
                    comando="INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
                    params=(gasto.data, gasto.valor, categoria_id),
                )

            return "Gasto adicionado com sucesso!"
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            raise

    def atualizar_gasto(self, gasto_id, categoria_nome, gasto: Gastos):
        with DBTransactionManager() as db_manager:
            db_manager.executar_transacao(
                comando="UPDATE Gastos SET data = ?, valor = ? WHERE id = ?",
                params=(gasto.data, gasto.valor, gasto_id),
            )

            db_manager.executar_transacao(
                comando="UPDATE Categorias SET nome = ? WHERE id = (SELECT categoria_id FROM Gastos WHERE id = ? LIMIT 1);",
                params=(categoria_nome, gasto_id),
            )

        return "Gasto atualizado com sucesso!"

    def listar_gastos(self, gastos: Gastos):
        with DBTransactionManager() as db_manager:

            if gastos.id is not None:
                resultado = db_manager.executar_transacao(
                    comando="SELECT Gastos.id AS gasto_id, data, valor, Categorias.nome AS categoria_nome "
                    "FROM Gastos "
                    "JOIN Categorias ON Gastos.categoria_id = Categorias.id WHERE gasto_id = ?",
                    params=(gastos.id,),
                )
            else:
                # Corrigir a concatenação das partes da consulta SQL
                resultado = db_manager.executar_transacao(
                    comando="SELECT Gastos.id AS gasto_id, data, valor, Categorias.nome AS categoria_nome "
                    "FROM Gastos "
                    "JOIN Categorias ON Gastos.categoria_id = Categorias.id"
                )

        # Verificar se a consulta retornou algum resultado
        if resultado:
            # Transformar os resultados em uma lista de dicionários
            gastos = [
                {
                    "id": row[0],
                    "data": row[1],
                    "valor": row[2],
                    "categoria_nome": row[3],
                }
                for row in resultado
            ]
            return gastos

        # Caso não tenha resultados, retornar uma lista vazia
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
