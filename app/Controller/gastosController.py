# app/controllers/gastosController.py
from flask import render_template, request, redirect

from app.Model.categoriasModel import (
    CategoriasDB,
    # Categorias,
)

from app.Model.gastosModel import (
    GastosDB,
    Gastos,
    Categorias,
)

class GastosController:
    # Static variable initialized as 0
    exibir_em_horas = 0

    @staticmethod
    def get_gastos(CPF):
        gasto = Gastos(id=None)
        gasto_db = GastosDB()
        gastos = gasto_db.listar_gastos(gasto, CPF)
        return render_template("gastos.html",gastos=gastos)

    @staticmethod
    def add_gasto(CPF):
        data = request.form.get("data")
        valor = request.form.get("valor")
        categoria_nome = request.form.get("categoria_nome")
        gasto = Gastos(data=data, valor=valor)
        gasto_db = GastosDB()
        categoria = Categorias(nome=categoria_nome)
        gasto_db.registrar_gasto_com_transacao(gasto, categoria, CPF)
        return redirect("/gastos")

    def update_gasto(gasto_id, CPF):
        gasto_db = GastosDB()

        if request.method == "POST":
            data = request.form.get("data")
            valor = request.form.get("valor")
            categoria_nome = request.form.get("categoria_nome")

            gasto = Gastos(data=data, valor=valor, id=gasto_id)
            gasto_db.atualizar_gasto(categoria_nome, gasto)
            return redirect("/gastos")

        gasto = Gastos(id=gasto_id)  # Criando um objeto Gastos com o ID fornecido
        gastos = gasto_db.listar_gastos(gasto, CPF)  # Busca os gastos no banco

        if not gastos:  # Caso não encontre o gasto
            return "Gasto não encontrado", 404

        # Garantir que estamos passando um único gasto (o primeiro da lista)
        gasto = gastos[0]  # Pegue o primeiro gasto

        # Obtenha a lista de categorias
        categorias = CategoriasDB.listar_categorias()

        return render_template("edit_gasto.html", gasto=gasto, categorias=categorias)

    @staticmethod
    def delete_gasto(gasto_id):
        gasto_db = GastosDB()
        gasto_db.deletar_gasto(gasto_id)
        return redirect("/gastos")