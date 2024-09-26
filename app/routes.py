from app import app
from flask import render_template, request, flash, redirect
from app.Controller.usuario import listarUsuario, verificarUsuario, adicionarUsuario, atualizarUsuario, deletarUsuario, feature2Logica
from app.Controller.usuario import feature1Logica,  feature2Logica
from app.Controller.gastosController import *

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

######Mudar aqui
@app.route('/feature1', methods=['GET', 'POST'])
def feature1():
    valor1 = request.form.get('valor1')
    valor2 = request.form.get('valor2')
    valor3 = request.form.get('valor3')
    valor4 = request.form.get('valor4')

    saida = feature1Logica(valor1, valor2, valor3, valor4)
    flash(saida)
    return render_template('feature2.html')

@app.route('/feature2', methods=['GET', 'POST'])
def feature2():
    valor1 = request.form.get('valor1')
    valor2 = request.form.get('valor2')
    valor3 = request.form.get('valor3')
    valor4 = request.form.get('valor4')

    saida = feature2Logica(valor1, valor2, valor3, valor4)
    flash(saida)
    return render_template('feature2.html')

@app.route('/gastos', methods=['GET','POST'])
def gastos():


    
    # if request.method == 'POST':
    #      if 'action' in request.form:
    #         action = request.form.get('action')
    #         if action == 'add':
    #             # Lógica para adicionar um novo gasto
    #             data = request.form.get('data')
    #             valor = request.form.get('valor')
    #             categoria_nome = request.form.get('categoria_nome')
    #             gastosController.create_gasto (data, valor, categoria_nome) #ver
    #             return redirect(url_for('gastos'))
            
    #         elif action == 'delete':
    #             # Lógica para deletar um gasto
    #             gasto_id = request.form.get('gasto_id')
    #             gastosController.delete_gasto(gasto_id)
    #             return redirect(url_for('gastos'))

    #         elif action == 'edit':
    #             # Lógica para atualizar um gasto
    #             gasto_id = request.form.get('gasto_id')
    #             data = request.form.get('data') # se não existir retorna None
    #             valor = request.form.get('valor')
    #             categoria_nome = request.form.get('categoria_nome')
    #             return gastosController.update_gasto(gasto_id,data,valor,categoria_nome)               
    # # vizuaizar os gastos
    # return gastosController.get_gastos()