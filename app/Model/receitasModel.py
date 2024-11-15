from dataclasses import dataclass
from datetime import date, datetime
from app.Model.databaseManager import DBTransactionManager, BaseDB

import sqlite3


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

    def registrar_receita_com_transacao(self, receita: Receita):
        with DBTransactionManager:
            self.registrar_receita_com_transacao(receita)

    def inserir_receita(self, receita: Receita):
        try:
            categoria = self._categoriaBD.resgatar_categoria_registrada(
                receita.categoria
            )
        except CategoriaNaoRegistrada:
            categoria = self._categoriaBD.adicionar_categoria(receita.categoria)

        self.salvar_receita_com_categoria(categoria, receita)

    def salvar_receita_com_categoria(self, categoria: Categoria, receita: Receita):
        self._db.executar_transacao(
            comando="INSERT INTO Receitas (data, valor, categoria_id) VALUES (?, ?, ?)",
            params=(receita.data_recebimento, receita.valor, categoria.id),
        )

    def obter_receita_por_id(self, receita_id: int):
        self._db.executar_transacao(
            comando=(
                "SELECT Receitas.id, Receitas.data, Receitas.valor, Categorias.nome"
                "AS categoria_nome"
                "FROM Receitas LEFT JOIN Categorias"
                "ON Receitas.categoria_id = Categorias.id"
                "WHERE Receitas.id = ?"
            ),
            params=(receita_id),
        )

    def listar_receitas(self, receita_id=None):
        if receita_id is not None:
            return self.listar_receita_unica(receita_id)
        else:
            return self.listar_todas_as_receitas()

    def listar_receita_unica(self, receita_id: int):
        receita = self._db.executar_transacao(
            comando=("SELECT * FROM Receitas WHERE id = ?", (receita_id)),
            fetchone=True,
        )
        return receita

    def listar_todas_as_receitas(self):
        receitas = self._db.executar_transacao(
            "SELECT * FROM Gastos",
        )
        return receitas
