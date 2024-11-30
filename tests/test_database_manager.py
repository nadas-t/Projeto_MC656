from dataclasses import dataclass
import unittest

from app.Model.databaseManager import BaseDB, DBTransactionManager


@dataclass
class TransacaoTest:
    def __init__(self, id: int, value: str):
        self._db = BaseDB()
        self.id = id
        self.value = value

    def executar_escrita(self):
        self._db.executar_transacao(
            comando="INSERT INTO TestTable (id, value) VALUES (?, ?)",
            params=(self.id, self.value),
        )

    def recuperar_escrita(self):
        result = self.db._executar_transacao(
            comando="SELECT * FROM TestTable WHERE value = ?",
            params=self.value,
            fetchone=True,
        )
        return result


class TransacaoPrincipalTest(TransacaoTest):
    def __init__(self, id: int, value: str, transacao_secundaria):
        self.transacao_secundaria = transacao_secundaria
        super().__init__(id, value)

    def executar_escrita(self):
        self.transacao_secundaria.executar_escrita()
        super().executar_escrita()


def get_line_from_value(value: str):
    with DBTransactionManager() as db:
        resultado = db.executar_transacao(
            comando="SELECT * FROM TestTable WHERE value = (?)",
            params=(value,),
            fetchone=True,
        )
        return resultado


class DBTest(unittest.TestCase):

    def setUp(self):
        with DBTransactionManager() as db:
            db.executar_transacao(
                comando="CREATE TABLE IF NOT EXISTS TestTable (id INTEGER PRIMARY KEY, value TEXT)",
            )

    def tearDown(self) -> None:
        with DBTransactionManager() as db:
            db.executar_transacao("DROP TABLE TestTable")


class TestDBManager(DBTest):

    def test_base_db_deve_ser_singletron(self):
        db1 = BaseDB()
        db2 = BaseDB()
        self.assertEqual(id(db1), id(db2))


class TestDBTransactionManager(DBTest):
    def test_escrita_no_banco_deve_persistir(self):
        t1 = TransacaoTest(id=1, value="test_id")
        esperado = (1, "test_id")
        with DBTransactionManager():
            t1.executar_escrita()

        resultado = get_line_from_value(t1.value)
        self.assertEqual(resultado, esperado)

    def test_escrita_de_instancias_distintas_deve_persistir(self):
        t1 = TransacaoTest(id=1, value="test_id1")
        t2 = TransacaoTest(id=2, value="test_id2")
        esperado1 = (1, "test_id1")
        esperado2 = (2, "test_id2")
        with DBTransactionManager():
            t1.executar_escrita()
            t2.executar_escrita()
        resultado1 = get_line_from_value(t1.value)
        resultado2 = get_line_from_value(t2.value)

        self.assertEqual(resultado1, esperado1)
        self.assertEqual(resultado2, esperado2)

    def test_escritas_dependentes_por_classe_associada_deve_persistir(self):
        t1 = TransacaoTest(id=1, value="test_id1")
        t2 = TransacaoPrincipalTest(id=2, value="test_id2", transacao_secundaria=t1)
        esperado1 = (1, "test_id1")
        esperado2 = (2, "test_id2")
        with DBTransactionManager():
            t2.executar_escrita()
        resultado1 = get_line_from_value(t2.transacao_secundaria.value)
        resultado2 = get_line_from_value(t2.value)

        self.assertEqual(resultado1, esperado1)
        self.assertEqual(resultado2, esperado2)

    def test_rollback_transacoes_de_instancias_distintas(self):
        t1 = TransacaoTest(id=1, value="test_id")
        t2 = TransacaoTest(id=1, value="duplicate_id_deve_falhar")
        with DBTransactionManager():
            t1.executar_escrita()
            t2.executar_escrita()

        resultado = get_line_from_value(t1.value)

        self.assertIsNone(resultado)

    def test_rollback_transacao_dependente_por_classes_associadas(self):
        t1 = TransacaoTest(id=1, value="test_id")
        t2 = TransacaoPrincipalTest(
            1, "duplicated_id_deve_falhar", transacao_secundaria=t1
        )
        with DBTransactionManager():
            t2.executar_escrita()
        resultado = get_line_from_value(t2.transacao_secundaria.value)

        self.assertIsNone(resultado)
