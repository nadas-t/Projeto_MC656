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
    def get_gastos():
        gasto = Gastos(id=None)
        gasto_db = GastosDB()
        gastos = gasto_db.listar_gastos(gasto)
        return render_template(
            "gastos.html",
            gastos=gastos,
            exibir_horas=GastosController.exibir_em_horas,
            salario_hora=87,
        )

    @staticmethod
    def add_gasto():
        data = request.form.get("data")
        valor = request.form.get("valor")
        categoria_nome = request.form.get("categoria_nome")
        gasto = Gastos(data=data, valor=valor)
        gasto_db = GastosDB()
        categoria = Categorias(nome=categoria_nome)
        gasto_db.adicionar_gasto(gasto, categoria)
        return redirect("/gastos")

    def update_gasto(gasto_id):
        gasto_db = GastosDB()

        if request.method == "POST":
            data = request.form.get("data")
            valor = request.form.get("valor")
            categoria_nome = request.form.get("categoria_nome")

            gasto = Gastos(data=data, valor=valor)
            gasto_db.atualizar_gasto(gasto_id, categoria_nome, gasto)
            return redirect("/gastos")

        gasto = Gastos(id=gasto_id)  # Criando um objeto Gastos com o ID fornecido
        gastos = gasto_db.listar_gastos(gasto)  # Busca os gastos no banco

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
