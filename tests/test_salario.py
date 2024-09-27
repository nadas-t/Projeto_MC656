import pytest
from unittest.mock import patch
from flask import Flask, flash
from app.Controller.salarioController import SalarioController  # Adjust the import based on your structure


@pytest.fixture
def client():
    app = Flask(__name__)
    app.secret_key = 'test'  # Required for session and flash
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_get_salario(client):
    # Test the rendering of the salary page
    response = SalarioController.get_salario()
    assert b'salario.html' in response.data  # Check if the response contains the template

def test_add_salario(client):
    # Mocking the request.form to simulate form data
    with patch('app.Controller.routes') as mock_request:
        mock_request.form = {
            'salario': '3000',
            'horas_trabalho': '40'
        }
        
        with patch('app.controllers.flash') as mock_flash:
            response = SalarioController.add_salario()
            
            # Check if the controller updated the class variables
            assert SalarioController.salario == 3000.0
            assert SalarioController.horas == 40.0
            
            # Check if flash was called
            mock_flash.assert_called_with('Salário e horas de trabalho atualizados com sucesso!')
            assert response.status_code == 302  # Check if redirected

def test_get_salario_hora(client):
    SalarioController.salario = 3000.0
    SalarioController.horas = 40.0
    salario_hora = SalarioController.get_salario_hora()
    
    # Check if the calculation is correct
    assert salario_hora == 75.0  # 3000 / 40
