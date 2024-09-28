# app/controllers/gastosController.py
from flask import render_template, request, redirect
from app.Model.categoriasModel import listar_categorias
from app.Model.gastosModel import (
    listar_gastos,
    adicionar_gasto,
    atualizar_gasto,
    deletar_gasto,
    converte_gasto_horas,
    obter_gasto_por_id
)
from app.Controller.salarioController import *

class GastosController:
    # Static variable initialized as 0
    exibir_em_horas = 0

    @staticmethod
    def get_gastos():
        gastos = listar_gastos()
        return render_template('gastos.html', gastos=gastos, exibir_horas = GastosController.exibir_em_horas, salario_hora = SalarioController.get_salario_hora())

    @staticmethod
    def add_gasto():
        data = request.form.get('data')
        valor = request.form.get('valor')
        categoria_nome = request.form.get('categoria_nome')
        adicionar_gasto(data, valor, categoria_nome)
        return redirect('/gastos')
    
    @staticmethod 
    def update_gasto(gasto_id):
        if request.method == 'POST':
            data = request.form.get('data')
            valor = request.form.get('valor')
            categoria_nome = request.form.get('categoria_nome')
            
            atualizar_gasto(gasto_id, data, valor, categoria_nome)
            return redirect('/gastos')

        gasto = listar_gastos(gasto_id)
        if gasto is None:
            return "Gasto não encontrado", 404

        # Obtenha a lista de categorias disponíveis
        categorias = listar_categorias()

        return render_template('edit_gasto.html', gasto=gasto, categorias=categorias)

    @staticmethod
    def delete_gasto(gasto_id):
        deletar_gasto(gasto_id)
        return redirect('/gastos')


















