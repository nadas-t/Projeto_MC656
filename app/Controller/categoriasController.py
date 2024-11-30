# app/controllers/categoriasController.py
from flask import render_template, request, redirect
from app.Model.categoriasModel import (
    Categorias,
    CategoriasDB,
)

class CategoriasController:
    @staticmethod
    def get_categorias():
        categorias = CategoriasDB().listar_categorias()
        #categorias = listar_categorias()
        return render_template('categorias.html', categorias=categorias)

    @staticmethod
    def add_categoria():
        nome = request.form.get('nome')

        categoria = Categorias(nome=nome)
        CategoriasDB().adicionar_categoria(categoria)
        return redirect('/categorias')
    
    @staticmethod
    def update_categoria(categoria_id):
        if request.method == 'POST':
            nome = request.form.get('nome')

            categorias = Categorias(id=categoria_id, nome=nome);
            CategoriasDB().atualizar_categoria(categorias)
            return redirect('/categorias')

        # Carregar os dados da categoria para edição
        categoria = CategoriasDB().listar_categorias(categoria_id)  # Você deve ter uma função para obter uma única categoria
        return render_template('updateCategoria.html', categoria=categoria)

    @staticmethod
    def delete_categoria(categoria_id):
        categorias = Categorias(id = categoria_id);
        CategoriasDB().deletar_categoria(categorias)
        return redirect('/categorias')