from app import app
from flask import render_template, request, flash, redirect, url_for
from app.Controller import categoriasController
from app.Controller.usuario import listarUsuario, verificarUsuario, adicionarUsuario, atualizarUsuario, deletarUsuario
from app.Controller.gastosController import *
from app.Controller.salarioController import *

@app.route('/')
@app.route('/index')

def index():
    nome = "Usuário"

    return render_template('/index.html', nome=nome)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario  = request.form.get('usuario')
    senha  = request.form.get('senha')

    if usuario == 'admin' and senha == 'senha123':
        return "Usuário {} e senha {}".format(usuario, senha)
    else:
        flash('Dados inválidos')
        return redirect('/login')

#Usuarios
@app.route('/usuarios')
def usuarios():
    rows = listarUsuario()
    return render_template('usuarios.html', rows=rows)

@app.route('/usuario', methods=['GET', 'POST'])
def usuario():
    row = {}  # Inicializa 'row' como um dicionário vazio

    if request.method == 'POST':
        CPF = request.form.get('CPF')
        nome = request.form.get('nome') 
        action = request.form.get('action') 
        idade = request.form.get('idade')
        email = request.form.get('email')        

        if CPF:
            result_list = verificarUsuario(CPF)  # Presume-se que verificarUsuario retorna uma lista

            if result_list:
                row = result_list[0]  # Assume que a lista contém ao menos um item e pega o primeiro item
                
                if action != 'edit':
                        resultado = atualizarUsuario(CPF, nome, idade, email)
                        flash(resultado)
                        return redirect('/usuario')
            else:
                resultado = adicionarUsuario(CPF, nome, idade, email)
                flash(resultado)
                return redirect('/usuario')

    return render_template('usuario.html', row=row)

@app.route('/deletarUsuario', methods=['POST'])
def removerUsuario():

    if request.method == 'POST':
        CPF = request.form.get('CPF')

        if (CPF != "") :
            # Código a ser executado se o valor de 'CPF' não for uma string vazia
            if verificarUsuario(CPF) is not None:
                resultado = deletarUsuario(CPF)
                flash(resultado)
                return redirect('/usuarios')
        else:
            flash('CPF em branco!')       
            
    return ""

# Rotas para Gastos
@app.route('/gastos', methods=['GET', 'POST'])
def gastos():
    if request.method == 'POST':
        return GastosController.add_gasto()
    return GastosController.get_gastos()

@app.route('/gastos/edit/<int:gasto_id>', methods=['GET', 'POST'])
def edit_gasto(gasto_id):
    return GastosController.update_gasto(gasto_id)



@app.route('/gastos/delete/<int:gasto_id>', methods=['POST'])
def delete_gasto(gasto_id):
    return GastosController.delete_gasto(gasto_id)

@app.route('/convert_gasto', methods=['POST'])
def convert_gasto():
    if GastosController.exibir_em_horas == 0:
        GastosController.exibir_em_horas = 1
    elif GastosController.exibir_em_horas == 1:
        GastosController.exibir_em_horas = 0
    return redirect(url_for('gastos'))  # Redirect back to the gastos page


# Rotas para Categorias
@app.route('/categorias', methods=['GET', 'POST'])
def categorias():
    if request.method == 'POST':
        return categoriasController.add_categoria()
    return categoriasController.get_categorias()

@app.route('/categorias/edit/<int:categoria_id>', methods=['GET', 'POST'])
def edit_categoria(categoria_id):
    return categoriasController.update_categoria(categoria_id)

@app.route('/categorias/delete/<int:categoria_id>', methods=['POST'])
def delete_categoria(categoria_id):
    return categoriasController.delete_categoria(categoria_id)


# Rotas para Salário
@app.route('/salario', methods=['GET', 'POST'])
def salario():
    if request.method == 'POST':
        return SalarioController.add_salario()
    return SalarioController.get_salario()

