from app import app
from flask import render_template, request, flash, redirect, url_for, session
from app.Controller import categoriasController
from app.Controller.usuarioController import *
from app.Controller.gastosController import GastosController, SalarioController
from app.Controller.salarioController import *

@app.route('/')
@app.route('/index')

def index():
    
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login')) 


@app.route('/login')
def login():

    if 'username' in session:
         return redirect(url_for('index')) 

    return render_template('usuario/login.html')

@app.route('/logout')
def logout():

    if 'username' in session:
         session.pop('username', None)
         return redirect(url_for('index')) 

    return render_template('usuario/login.html')

@app.route('/configuracao_conta', methods=['GET', 'POST'])
def configuracao_conta():

    if 'username' in session:
        
        if request.method == 'POST':
            
            CPF = request.form.get('CPF')
            nome = request.form.get('nome')  
            idade = request.form.get('idade')
            email = request.form.get('email')   

            resultado = atualizarUsuario(CPF, nome, idade, email, session['senha'])
            session['email'] = email
            session['username'] = nome

            flash(resultado)
            return redirect('/configuracao_conta')
        
        row = {}
        result_list = verificaLogin(session['email'], session['senha'])
        row = result_list[0]
        return render_template('usuario/configuracao_conta.html', row = row)

    return redirect(url_for('login')) 

@app.route('/trocar_senha', methods=['GET', 'POST'])
def trocar_senha():

    if 'username' in session:
        
        if request.method == 'POST':
            
            senha = request.form.get('senha')  
            senha1 = request.form.get('senha1')
            senha2 = request.form.get('senha2')

            resultado = atualizarSenha(session['email'], senha, senha1, senha2)
            if(resultado == "Senha atualizada com sucesso!"):
                session['senha'] = senha1

            flash(resultado)
            return redirect('/trocar_senha')
        
        if 'username' in session:
            return render_template('usuario/trocar_senha.html')

    return redirect(url_for('login')) 

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():

    if request.method == 'POST':
        CPF = request.form.get('CPF')
        nome = request.form.get('nome')  
        idade = request.form.get('idade')
        email = request.form.get('email')
        senha1 = request.form.get('senha1')        
        senha2 = request.form.get('senha2')

        resultado = adicionarUsuario(CPF, nome, idade, email, senha1, senha2)
        flash(resultado)

        if(resultado == 'Usuário cadastrado com sucesso!'):
            flash('Realize o login por favor')
            return redirect(url_for('registrar'))

    return render_template('usuario/registrar.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    email  = request.form.get('email')
    senha  = request.form.get('senha')

    result_list = verificaLogin(email, senha)  # Presume-se que verificarUsuario retorna uma lista
    
    if result_list:
        row = result_list[0]
        session['username'] = row['nome']
        session['email'] = email
        session['senha'] = senha
    else:
        flash('Usuário e/ou senha incorretos!')

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
        if 'adicionar_gasto' in request.form:
            return GastosController.add_gasto()
        
        elif 'converter_gasto' in request.form:
            return redirect('/convert_gasto')
        
    return GastosController.get_gastos()

@app.route('/gastos/edit/<int:gasto_id>', methods=['GET', 'POST'])
def edit_gasto(gasto_id):
    return GastosController.update_gasto(gasto_id)


@app.route('/gastos/delete/<int:gasto_id>', methods=['POST'])
def delete_gasto(gasto_id):
    return GastosController.delete_gasto(gasto_id)

@app.route('/convert_gasto', methods=['GET', 'POST'])
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

