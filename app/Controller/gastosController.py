from app.Model.gastosModel import (
    adicionar_gasto,
    listar_gastos,
    atualizar_gasto,
    deletar_gasto
)
from flask import render_template, request, redirect, url_for

class gastosController:
    @staticmethod
    def create_gasto(data,valor,categoria_nome):
            # Adiciona o gasto
        adicionar_gasto(data, valor, categoria_nome)
        return redirect('/gastos')
        

        # return render_template('gastos.html',)  # Exibe o formulário de adição de gasto

    @staticmethod
    def get_gastos():
        # Lista os gastos
        gastos = listar_gastos()
        return render_template('gastos.html', gastos=gastos)  # Renderiza a lista de gastos

    @staticmethod
    def update_gasto(gasto_id,data,valor,categoria_nome):
        if data is not None and valor is not None and categoria_nome is not None:
            # Atualiza o gasto
            atualizar_gasto(gasto_id, data, valor, categoria_nome)
            return redirect('/gastos')  # Redireciona para a lista de gastos
        # gasto = listar_gastos(gasto_id)  # Busca o gasto específico para exibição no formulário de edição
        return render_template('updateGasto.html', gasto_id=gasto_id)  # Renderiza o formulário de edição

    @staticmethod
    def delete_gasto(gasto_id):
        # Deleta o gasto
        resultado = deletar_gasto(gasto_id)
        return redirect('/gastos')  # Redireciona para a lista de gastos       #ver
