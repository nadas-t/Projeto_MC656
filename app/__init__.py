from flask import Flask
app = Flask(__name__, template_folder='View')
app.config['SECRET_KEY'] = "chave" #Mudar depois
from app import routes
from app.Controller.criaBanco import Cria

###Cria o banco de dados localmente
Cria()