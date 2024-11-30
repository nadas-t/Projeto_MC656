from dataclasses import dataclass
from app.Model.databaseManager import DBTransactionManager, BaseDB


class ErroAoCadastrarCategoria(Exception):
    pass


class NomeCategoriaInvalido(ErroAoCadastrarCategoria):
    pass


class CategoriaNaoRegistrada(Exception):
    pass


@dataclass
class Categorias:
    nome: str
    id: int = None

    def __post_init__(self):
        pass


class CategoriasDB:
    def __init__(self):
        self._db = BaseDB()

    def adicionar_categoria(self, categoria: Categorias, CPF):
        self._db.executar_transacao(
            comando="INSERT INTO Categorias (nome, usuarios_id) VALUES (?, ?)",
            params=(categoria.nome, CPF),
        )
        nova_categoria = self.resgatar_categoria(categoria, CPF)
        return nova_categoria

    def resgatar_categoria(self, categoria: Categorias, CPF):
        categoria_encontrada = self._db.executar_transacao(
            comando="SELECT id FROM Categorias WHERE nome = ? AND usuarios_id = ?",
            params=(categoria.nome, CPF),

            fetchone=True,
        )
        return categoria_encontrada

    def resgatar_categoria_registrada(self, categoria: Categorias, CPF):
        categoria_encontrada = self.resgatar_categoria(categoria, CPF)

        if not categoria_encontrada:
            raise CategoriaNaoRegistrada(
                f'A categoria "{categoria.nome}" ainda não está '
                f"registrada no sistema"
            )
        return categoria_encontrada

    def vincular_categoria(self, categoria: Categorias, CPF):
        try:
            categoria = self.resgatar_categoria_registrada(categoria, CPF)
        except CategoriaNaoRegistrada:
            categoria = self.adicionar_categoria(categoria, CPF)

        categoria_id = categoria[0]
        return categoria_id

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
