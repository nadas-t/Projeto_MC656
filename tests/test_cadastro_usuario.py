import pytest
from unittest.mock import patch
from flask import Flask, flash, url_for
from app.Controller.salarioController import SalarioController  # Adjust the import based on your structure
from app.Controller.gastosController import GastosController
from app.Controller.usuario import adicionarUsuario, deletarUsuario, atualizarUsuario

@pytest.fixture
def client():
    app = Flask(__name__)
    app.secret_key = 'test'  # Required for session and flash
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_add_usuario(client):
    # Create an application context
    with client.application.app_context():
        # Mocking the request.form to simulate form data
        with client.application.test_request_context('/usuario', method='POST', data={'CPF': '200', 'nome': 'teste', 'idade': '25', 'email': 'email@email.com'}):
            # Capture the form data from the request context
            data = {
                'CPF': '200',
                'nome': 'teste',
                'idade': '25',
                'email': 'email@email.com'
            }

            # Mocking flash to suppress output during the test
            with patch('flask.flash') as mock_flash:
                # Call the function with the captured form data
                retorno = adicionarUsuario(data['CPF'], data['nome'], data['idade'], data['email'])

                # Verify the function returns the expected string
                assert isinstance(retorno, str)  # Check if it is a string
                assert retorno == "Usuário cadastrado com sucesso!"

def test_update_usuario(client):
    # Create an application context
    with client.application.app_context():
        # Mocking the request.form to simulate form data
        with client.application.test_request_context('/usuario', method='POST', data={'CPF': '200', 'nome': 'teste', 'idade': '25', 'email': 'email@email.com'}):
            # Capture the form data from the request context
            data = {
                'CPF': '200',
                'nome': 'teste2',
                'idade': '26',
                'email': 'email2@email.com'
            }

            # Mocking flash to suppress output during the test
            with patch('flask.flash') as mock_flash:
                # Call the function with the captured form data
                retorno = atualizarUsuario(data['CPF'], data['nome'], data['idade'], data['email'])

                # Verify the function returns the expected string
                assert isinstance(retorno, str)  # Check if it is a string
                assert retorno == "Usuário atualizado com sucesso!"

def test_delete_usuario(client):
    # Create an application context
    with client.application.app_context():
        # Mocking the request.form to simulate form data
        with client.application.test_request_context('/usuario', method='POST', data={'CPF': '200'}):
            # Capture the form data from the request context
            data = {
                'CPF': '200'
            }

            # Mocking flash to suppress output during the test
            with patch('flask.flash') as mock_flash:
                # Call the function with the captured form data
                retorno = deletarUsuario(data['CPF'])

                # Verify the function returns the expected string
                assert isinstance(retorno, str)  # Check if it is a string
                assert retorno == "Usuário removido com sucesso!"