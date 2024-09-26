# app/controllers/categoriasController.py
from flask import render_template, request, redirect
from app.Model.categoriasModel import (
    listar_categorias,
    adicionar_categoria,
    atualizar_categoria,
    deletar_categoria
)

class CategoriasController:
    @staticmethod
    def get_categorias():
        categorias = listar_categorias()
        return render_template('categorias.html', categorias=categorias)

    @staticmethod
    def add_categoria():
        nome = request.form.get('nome')
        adicionar_categoria(nome)
        return redirect('/categorias')

    @staticmethod
    def update_categoria(categoria_id):
        if request.method == 'POST':
            nome = request.form.get('nome')
            atualizar_categoria(categoria_id, nome)
            return redirect('/categorias')

        # Carregar os dados da categoria para edição
        categoria = listar_categorias(categoria_id)  # Você deve ter uma função para obter uma única categoria
        return render_template('updateCategoria.html', categoria=categoria)

    @staticmethod
    def delete_categoria(categoria_id):
        deletar_categoria(categoria_id)
        return redirect('/categorias')























# from flask import request, render_template, redirect, url_for
# from app.Model.categoriasModel import (
#     adicionar_categoria,
#     listar_categorias,
#     atualizar_categoria,
#     deletar_categoria,
# )
# class categoriasController:
#     @staticmethod
#     def create_categoria():
#         nome = request.form.get('nome')  # Usar request.form para dados de formulário
#         resultado = adicionar_categoria(nome)
#         return redirect(url_for('read_categorias'))  # Redireciona para a lista de categorias
#     @staticmethod
#     def read_categorias():
#         categorias = listar_categorias()
#         return render_template('categorias/listar.html', categorias=categorias)  # Renderiza um template
#     @staticmethod
#     def update_categoria(id):
#         nome = request.form.get('nome')  # Usar request.form para dados de formulário
#         resultado = atualizar_categoria(id, nome)
#         return redirect(url_for('read_categorias'))  # Redireciona para a lista de categorias
#     @staticmethod
#     def delete_categoria(id):
#         resultado = deletar_categoria(id)
#         return redirect(url_for('read_categorias'))  # Redireciona para a lista de categorias
