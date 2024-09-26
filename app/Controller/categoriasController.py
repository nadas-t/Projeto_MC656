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





















