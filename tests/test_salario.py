import pytest
from unittest.mock import patch
from flask import Flask, flash, url_for
from app.Controller.salarioController import SalarioController  # Adjust the import based on your structure
from app.Controller.gastosController import GastosController

@pytest.fixture
def client():
    app = Flask(__name__)
    app.secret_key = 'test'  # Required for session and flash
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_add_salario(client):
    # Create an application context
    with client.application.app_context():
        # Mocking the request.form to simulate form data
        # Create a request context
        with client.application.test_request_context('/salario', method='POST', data={'salario': '3000', 'horas_trabalho': '40'}):
            
            with patch('flask.flash') as mock_flash:
                response = SalarioController.add_salario()
                
                # Check if the controller updated the class variables
                assert SalarioController.salario == 3000.0
                assert SalarioController.horas == 40.0

def test_add_salario_non_positive(client):
    # Create an application context
    with client.application.app_context():
        # Mocking the request.form to simulate form data
        # Create a request context
        with client.application.test_request_context('/salario', method='POST', data={'salario': '0', 'horas_trabalho': '-40'}):
            
            with patch('flask.flash') as mock_flash:
                response = SalarioController.add_salario()
                
                # Check if the controller updated the class variables
                assert SalarioController.salario != 0
                assert SalarioController.horas != 0

def test_get_salario(client):
    # Set the class variables
    SalarioController.salario = 3000.0
    SalarioController.horas = 40.0

    # Create an application context
    with client.application.app_context():
        # Create a request context
        with client.application.test_request_context('/salario', method='GET'):
            # Mocking the render_template function
            with patch('app.Controller.salarioController.render_template', return_value="Rendered Template") as mock_render_template:
                response = SalarioController.get_salario()
                
                # Check if render_template was called with the correct arguments
                mock_render_template.assert_called_with('salario.html', salario=3000.0, horas_trabalho=40.0)

def test_get_salario_hora(client):
    # Create an application context
    with client.application.app_context():
        SalarioController.salario = 3000.0
        SalarioController.horas = 40.0
        salario_hora = SalarioController.get_salario_hora()
        
        # Check if the calculation is correct
        assert salario_hora == 75.0  # 3000 / 40