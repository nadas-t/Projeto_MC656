import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized

from app.Model.limitesModel import LimiteGastos
from app.Model.monitoramento.limiteGastos import  MonitoramentoLimiteGastos
from datetime import datetime

class TestGerarAlertaDeLimiteDeGastos(unittest.TestCase):
    @parameterized.expand([
        (1000.00, 1000.00, "Grave"),
        (1000.00, 999.99, "Média"),
        (1000.00, 800.00, "Média"),
        (1000.00, 799.99, "Baixa"),
        (1000.00, 500.00, "Baixa"),
    ])
    @patch("app.Model.monitoramento.limiteGastos.MonitoramentoLimiteGastos.limite_atual")
    def test_gerar_alerta_por_severidade(self, limite, total_gasto, severidade_esperada,  mock_limite_atual):
        mock_limite_atual.return_value = LimiteGastos(
            valor=limite,
            data_expiracao=datetime.strptime("2024-02-17", "%Y-%m-%d").date(),
            data_inicio=datetime.strptime("2024-02-16", "%Y-%m-%d").date(),
        )
        monitor_limite = MonitoramentoLimiteGastos("foo")
        
        gerador_alerta = monitor_limite.gerar_alerta(total_gasto)
        severidade = gerador_alerta.exibir_severidade()
        self.assertEqual(severidade, severidade_esperada)
        
class TestMonitorGastos(unittest.TestCase):
    
    @patch("app.Model.gastosModel.GastosDB.listar_gastos")
    @patch("app.Model.monitoramento.limiteGastos.MonitoramentoLimiteGastos.limite_atual")
    def test_calcular_total_gastos(self, mock_limite_atual, mock_listar_gastos):
        # Mockando os gastos retornados pelo método listar_gastos
        mock_listar_gastos.return_value = [
            {"id": 1, "data": "2024-02-15", "valor": 250.00, "categoria": "Transporte"},
            {"id": 2, "data": "2024-02-16", "valor": 150.00, "categoria": "Alimentação"},
            {"id": 3, "data": "2024-02-17", "valor": 300.00, "categoria": "Lazer"},
            {"id": 4, "data": "2024-02-18", "valor": 100.00, "categoria": "Educação"},
            {"id": 5, "data": "2024-02-19", "valor": 200.00, "categoria": "Saúde"},
            {"id": 6, "data": "2024-02-20", "valor": 200.00, "categoria": "Saúde"},
        ]
        # Mockando o limite atual como None (não é relevante neste teste)
        mock_limite_atual.return_value = LimiteGastos(
            valor=915.00,
            data_expiracao=datetime.strptime("2024-02-17", "%Y-%m-%d").date(),
            data_inicio=datetime.strptime("2024-02-16", "%Y-%m-%d").date(),
        )
        
        # Instanciando o monitor
        monitor_gastos = MonitoramentoLimiteGastos("foo")
        
        # Definindo o intervalo de datas
        data_min = datetime.strptime("2024-02-16", "%Y-%m-%d").date()
        data_max = datetime.strptime("2024-02-19", "%Y-%m-%d").date()
        
        # Chamando o método e verificando o resultado
        total = monitor_gastos.get_total_gasto_no_intervalo(data_min, data_max)
        self.assertEqual(total, 750.00)  # Soma dos valores no intervalo fornecido
