from flask import request, render_template, redirect, url_for
from app.Model.categoriasModel import (
    adicionar_categoria,
    listar_categorias,
    atualizar_categoria,
    deletar_categoria,
)
class categoriasController:
    @staticmethod
    def create_categoria():
        nome = request.form.get('nome')  # Usar request.form para dados de formulário
        resultado = adicionar_categoria(nome)
        return redirect(url_for('read_categorias'))  # Redireciona para a lista de categorias
    @staticmethod
    def read_categorias():
        categorias = listar_categorias()
        return render_template('categorias/listar.html', categorias=categorias)  # Renderiza um template
    @staticmethod
    def update_categoria(id):
        nome = request.form.get('nome')  # Usar request.form para dados de formulário
        resultado = atualizar_categoria(id, nome)
        return redirect(url_for('read_categorias'))  # Redireciona para a lista de categorias
    @staticmethod
    def delete_categoria(id):
        resultado = deletar_categoria(id)
        return redirect(url_for('read_categorias'))  # Redireciona para a lista de categorias
