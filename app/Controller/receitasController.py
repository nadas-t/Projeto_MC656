# app/controllers/gastosController.py
from flask import render_template, request, redirect

from app.Model.categoriasModel import (
    CategoriasDB,
)

from app.Model.receitasModel import (
    ReceitasDB,
    Receitas,
    Categorias,
)

class ReceitasController:
    # Static variable initialized as 0
    exibir_em_horas = 0

    @staticmethod
    def get_receitas(CPF):
        receita = Receitas(id=None)
        receitas_db = ReceitasDB()
        receitas = receitas_db.listar_receitas(receita, CPF)
        return render_template("receitas.html",receitas=receitas)

    @staticmethod
    def add_receita(CPF):
        data = request.form.get("data")
        valor = request.form.get("valor")
        categoria_nome = request.form.get("categoria_nome")
        receita = Receitas(data=data, valor=valor)
        receita_db = ReceitasDB()
        categoria = Categorias(nome=categoria_nome)
        receita_db.registrar_receita_com_transacao(receita, categoria, CPF)
        return redirect("/receitas")

    def update_receita(receita_id, CPF):
        receita_db = ReceitasDB()

        if request.method == "POST":
            data = request.form.get("data")
            valor = request.form.get("valor")
            categoria_nome = request.form.get("categoria_nome")

            receita = Receitas(data=data, valor=valor, id=receita_id)
            receita_db.atualizar_receita(categoria_nome, receita)
            return redirect("/receitas")

        receita = Receitas(id=receita_id)  # Criando um objeto Gastos com o ID fornecido
        receitas = receita_db.listar_receitas(receita, CPF)  # Busca os gastos no banco

        if not receitas:  # Caso não encontre o gasto
            return "Receita não encontrada", 404

        # Garantir que estamos passando um único gasto (o primeiro da lista)
        receita = receitas[0]  # Pegue o primeiro gasto

        # Obtenha a lista de categorias
        categorias = CategoriasDB.listar_categorias()

        return render_template("edit_receita.html", receita=receita, categorias=categorias)

    @staticmethod
    def delete_receita(receita_id):
        receita_db = ReceitasDB()
        receita_db.deletar_receita(receita_id)
        return redirect("/receitas")