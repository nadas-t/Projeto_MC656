import unittest
from unittest.mock import patch
from flask import Flask, flash, url_for
from app.Controller.salarioController import SalarioController  # Adjust the import based on your structure
from app.Controller.gastosController import GastosController
from parameterized import parameterized

class SalarioTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'test'  # Required for session and flash
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    @parameterized.expand([
        ("valid_salary", {'salario': '3000', 'horas_trabalho': '40'}, 3000.0, 40.0),
        ("zero_salary", {'salario': '0', 'horas_trabalho': '40'}, None, None),
        ("negative_salary", {'salario': '-3000', 'horas_trabalho': '40'}, None, None),
        ("zero_hours", {'salario': '3000', 'horas_trabalho': '0'}, None, None),
        ("negative_hours", {'salario': '3000', 'horas_trabalho': '-40'}, None, None),
    ])
    def test_add_salario_parametrized(self, name, data, expected_salario, expected_horas):
        salarioInicial = SalarioController.salario
        horasInicial = SalarioController.horas
        with self.app.app_context():
            with self.app.test_request_context('/salario', method='POST', data=data):
                with patch('flask.flash') as mock_flash:
                    response = SalarioController.add_salario()
                    
                    if expected_salario is not None and expected_horas is not None:
                        self.assertEqual(SalarioController.salario, expected_salario)
                        self.assertEqual(SalarioController.horas, expected_horas)
                    else:
                        self.assertEqual(SalarioController.salario, salarioInicial)
                        self.assertEqual(SalarioController.horas, horasInicial)

    def test_get_salario(self):
        SalarioController.salario = 3000.0
        SalarioController.horas = 40.0

        with self.app.app_context():
            with self.app.test_request_context('/salario', method='GET'):
                with patch('app.Controller.salarioController.render_template', return_value="Rendered Template") as mock_render_template:
                    response = SalarioController.get_salario()
                    
                    # Check if render_template was called with the correct arguments
                    mock_render_template.assert_called_with('salario.html', salario=3000.0, horas_trabalho=40.0)

    def test_get_salario_hora(self):
        with self.app.app_context():
            SalarioController.salario = 3000.0
            SalarioController.horas = 40.0
            salario_hora = SalarioController.get_salario_hora()
            
            # Check if the calculation is correct
            self.assertEqual(salario_hora, 75.0)  # 3000 / 40

if __name__ == '__main__':
    unittest.main()