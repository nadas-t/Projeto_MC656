import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized

from app.Model.monitoramento.limiteGastos import MonitoramentoLimiteGastos

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
        mock_limite_atual.return_value = limite
        monitor_limite = MonitoramentoLimiteGastos("foo")
        
        gerador_alerta = monitor_limite.gerar_alerta(total_gasto)
        severidade = gerador_alerta.exibir_severidade()
        self.assertEqual(severidade, severidade_esperada)