from app.Model.configBancoModel import conexao


class ErroNaComunicacaoComDB(Exception):
    pass


class DBTransactionManager:
    """
    Context manager responsável por estabelecer a conexão com o banco
    através da intanciação única do singletron BaseDB, compartilhada
    entre todos os módulos envolvidos no mesmo conjunto relacionado de
    transações.
    Ao encerrar do contexto a conexão com o banco é desfeita, assim como
    a instância de BaseDB, neste momento todas as operações pendentes
    são gravadas de forma permanente.
    """

    def __init__(self):
        self.db = BaseDB()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.db.cancelar_transacao()
        else:
            self.db.commit()
        if self.db:
            self.db.close()
        return True


class BaseDBMetaclass(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]


class BaseDB(metaclass=BaseDBMetaclass):
    def __init__(self):
        self._conn = conexao()
        self._cur = self._conn.cursor()

    def cancelar_transacao(self):
        self._conn.rollback()

    def commit(self):
        self._conn.commit()

    def executar_transacao(self, comando, params=(), fetchone=False, row_fatory=None):
        if row_fatory:
            self._conn.row_factory = row_fatory
        try:
            self._cur.execute(comando, params)
            if fetchone:
                return self._cur.fetchone()
            return self._cur.fetchall()

        except Exception as exc:
            raise ErroNaComunicacaoComDB(
                f"Não foi possível concluir a transação: {exc}"
            )

    def close(self):
        cls = self.__class__
        self._conn.close()
        cls._instance = {}
