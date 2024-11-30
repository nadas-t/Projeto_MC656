from app.Model.databaseManager import BaseDB, DBTransactionManager


class InstanciadorDB:
    def __init__(self):
        self._db = BaseDB()

    def gerar_tabela_de_categorias(self):
        self._db.executar_transacao(
            comando="""
                CREATE TABLE IF NOT EXISTS categorias (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL UNIQUE
                )
                """
        )

    def gerar_tabela_de_gastos(self):
        self._db.executar_transacao(
            comando="""
                CREATE TABLE IF NOT EXISTS Gastos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT NOT NULL,
                    valor REAL NOT NULL,
                    categoria_id INTEGER,
                    FOREIGN KEY (categoria_id) REFERENCES categorias (id)
                )
                """
        )

    def gerar_tabela_de_usuarios(self):
        self._db.executar_transacao(
            comando="""
                CREATE TABLE IF NOT EXISTS Usuario (
                    CPF INTEGER PRIMARY KEY AUTOINCREMENT,  
                    nome TEXT NOT NULL, 
                    idade INTEGER NOT NULL, 
                    email TEXT UNIQUE NOT NULL,
                    senha TEXT NOT NULL,
                    limite REAL,
                    salario REAL,
                    horas_trabalho REAL
                )"""
        )

    def CriarBancoDados(self):
        with DBTransactionManager():
            self.gerar_tabela_de_categorias()
            self.gerar_tabela_de_gastos()
            self.gerar_tabela_de_usuarios()
