import unittest
from unittest.mock import MagicMock, patch
from app.Model.gastosModel import Gastos, GastosDB, converte_gasto_horas
from app.Model.categoriasModel import Categorias

class TestConverteGastoHoras(unittest.TestCase):
    def test_converte_gasto_horas(self):
        # Dados de entrada
        gastos = [
            Gastos(data="2024-12-01", valor=200.0, id=1, categoria=Categorias(nome="Transporte")),
            Gastos(data="2024-12-01", valor=300.0, id=2, categoria=Categorias(nome="Alimentação")),
        ]
        ganho_por_hora = 50.0

        # Executa a função
        resultado = converte_gasto_horas(gastos, ganho_por_hora)

        # Verifica os resultados
        self.assertEqual(resultado[0].valor, 4.0)  # 200 / 50
        self.assertEqual(resultado[1].valor, 6.0)  # 300 / 50
        
class TestGastosDB(unittest.TestCase):
    def setUp(self):
        # Configuração inicial
        self.gastos_db = GastosDB()
        self.gastos_db._db = MagicMock()
    
    def test_registrar_gasto(self):
        # Simula a inserção de um gasto
        gasto = Gastos(data="2024-12-01", valor=150.0, id=1)
        CPF = "12345678900"
        categoria_id = 2

        self.gastos_db.registrar_gasto(categoria_id, gasto, CPF)

        self.gastos_db._db.executar_transacao.assert_called_once_with(
            comando="INSERT INTO Gastos (data, valor, categoria_id, usuario_id) VALUES (?, ?, ?, ?)",
            params=("2024-12-01", 150.0, 2, "12345678900"),
        )
    
    def test_atualizar_gasto(self):
        gasto = Gastos(data="2024-12-02", valor=200.0, id=1)
        categoria_nome = "Educação"

        resultado = self.gastos_db.atualizar_gasto(categoria_nome, gasto)

        self.assertEqual(resultado, "Gasto atualizado com sucesso!")

    '''Revisar depois 
    def test_deletar_gasto(self):
        gasto_id = 1

        resultado = self.gastos_db.deletar_gasto(gasto_id)

        self.gastos_db._db.executar_transacao.assert_called_once_with(
            comando="DELETE FROM Gastos WHERE id = ?",
            params=(gasto_id,),
        )
        self.assertEqual(resultado, "Gasto deletado com sucesso!")
    '''