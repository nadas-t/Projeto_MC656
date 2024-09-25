from app.Model.gastosModel import (
    criar_tabela_gastos,
    adicionar_gasto,
    listar_gastos,
    atualizar_gasto,
    deletar_gasto
)
from flask import render_template, request, redirect, url_for

class gastosController:
    @staticmethod
    def create_gasto():
        if request.method == 'POST':
            # Pega os dados do formulário
            data_gasto = request.form.get('data')
            valor = request.form.get('valor')
            categoria_id = request.form.get('categoria_id')

            # Adiciona o gasto
            resultado = adicionar_gasto(data_gasto, valor, categoria_id)
            return redirect(url_for('gastos_controller.get_gastos'))  # Redireciona para a lista de gastos

        return render_template('gastos.html',)  # Exibe o formulário de adição de gasto

    @staticmethod
    def get_gastos():
        # Lista os gastos
        gastos = listar_gastos()
        return render_template('gastos/listar.html', gastos=gastos)  # Renderiza a lista de gastos

    @staticmethod
    def update_gasto(gasto_id):
        if request.method == 'POST':
            # Pega os dados do formulário
            data_gasto = request.form.get('data')
            valor = request.form.get('valor')
            categoria_id = request.form.get('categoria_id')

            # Atualiza o gasto
            resultado = atualizar_gasto(gasto_id, data_gasto, valor, categoria_id)
            return redirect(url_for('gastos_controller.get_gastos'))  # Redireciona para a lista de gastos

        gasto = listar_gastos(gasto_id)  # Busca o gasto específico para exibição no formulário de edição
        return render_template('gastos/editar.html', gasto=gasto)  # Renderiza o formulário de edição

    @staticmethod
    def delete_gasto(gasto_id):
        # Deleta o gasto
        resultado = deletar_gasto(gasto_id)
        return redirect(url_for('gastos_controller.get_gastos'))  # Redireciona para a lista de gastos
