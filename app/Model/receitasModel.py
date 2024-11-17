from dataclasses import dataclass
from datetime import date, datetime
from app.Model.databaseManager import DBTransactionManager, BaseDB


class ErroAoCadastrarReceita(Exception):
    pass


class ValorDeReceitaInsulficiente(ErroAoCadastrarReceita):
    pass


class ErroAoCadastrarCategoria(Exception):
    pass


class NomeCategoriaInvalido(ErroAoCadastrarCategoria):
    pass


class CategoriaNaoRegistrada(Exception):
    pass


@dataclass
class Categoria:
    nome: str
    id: int = None

    def __post_init__(self):
        self.validar_instancia()

    def validar_instancia(self):
        if not self.nome:
            raise NomeCategoriaInvalido("Não é possível criar uma categoria vazia!")


@dataclass
class Receita:
    data_recebimento: date
    categoria: Categoria
    valor: float
    data_cadastro: date = datetime.now()
    id: int = None

    def __post_init__(self):
        self.validar_instancia()

    def validar_instancia(self):
        if self.valor <= 0:
            raise ValorDeReceitaInsulficiente(
                f'"{self.valor}" é insulficiente para criação da receita!'
            )


class CategoriaDB:
    def __init__(self):
        self._db = BaseDB()

    def resgatar_categoria(self, categoria: Categoria):
        categoria_encontrada = self._db.executar_transacao(
            comando="SELECT id FROM Categorias WHERE nome = ?",
            params=(categoria.nome,),
            fetchone=True,
        )
        return categoria_encontrada

    def adicionar_categoria(self, categoria: Categoria):
        self._db.executar_transacao(
            comando="INSERT INTO Categorias (nome) VALUES (?)",
            params=(categoria.nome,),
            commit=True,
        )
        nova_categoria = self.resgatar_categoria(categoria)
        return nova_categoria

    def resgatar_categoria_registrada(self, categoria: Categoria):
        categoria_encontrada = self.resgatar_categoria(categoria)
        if not categoria_encontrada:
            raise CategoriaNaoRegistrada(
                f'A categoria "{categoria.nome}" ainda não está '
                f"registrada no sistema"
            )
        return categoria_encontrada


class ReceitaDB:
    def __init__(self):
        self._db = BaseDB()
        self._categoriaBD = CategoriaDB()

    def transacao_registrar_receita(
        self, receita: Receita
    ):  # TODO pensar em um nome melhor
        with DBTransactionManager:
            self.adicionar_receita(receita)

    def adicionar_receita(self, receita: Receita):
        try:
            categoria = self._categoriaBD.resgatar_categoria_registrada(
                receita.categoria
            )
        except CategoriaNaoRegistrada:
            categoria = self._categoriaBD.adicionar_categoria(receita.categoria)

        self.registrar_receita(categoria, receita)

    def registrar_receita(self, categoria: Categoria, receita: Receita):
        self._db.executar_transacao(
            comando="INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            params=(receita.data_recebimento, receita.valor, categoria.id),
        )

    def obter_receita_por_id(self, receita_id: int):
        self._db.executar_transacao(
            comando=(
                "SELECT Gastos.id, Gastos.data, Gastos.valor, Categorias.nome"
                "AS categoria_nome"
                "FROM Gastos LEFT JOIN Categorias"
                "ON Gastos.categoria_id = Categorias.id"
                "WHERE Gastos.id = ?"
            ),
            params=(receita_id),
        )
