from flask import Flask
from app.Controller.configBanco import Cria

# Cria a instância da aplicação Flask
app = Flask(__name__, template_folder='View')

# Configurações da aplicação
app.config['SECRET_KEY'] = "Ro5&B+agkatMy9cG1fLeq@Sfvn607by4" #chave para oroteger os dados

###Cria o banco de dados localmente
Cria()

# Importa as rotas (deve ser feito depois da configuração da app)
from app import routes