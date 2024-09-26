# app/controllers/gastosController.py
from flask import render_template, request, redirect
from app.Model.categoriasModel import listar_categorias
from app.Model.gastosModel import (
    listar_gastos,
    adicionar_gasto,
    atualizar_gasto,
    deletar_gasto,
    obter_gasto_por_id
)

class GastosController:
    @staticmethod
    def get_gastos():
        gastos = listar_gastos()
        return render_template('gastos.html', gastos=gastos)

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






















# from app.Model.gastosModel import (
#     adicionar_gasto,
#     listar_gastos,
#     atualizar_gasto,
#     deletar_gasto
# )
# from flask import render_template, request, redirect, url_for

# class gastosController:
#     @staticmethod
#     def create_gasto(data,valor,categoria_nome):
#             # Adiciona o gasto
#         adicionar_gasto(data, valor, categoria_nome)
#         return redirect('/gastos')
        

#         # return render_template('gastos.html',)  # Exibe o formulário de adição de gasto

#     @staticmethod
#     def get_gastos():
#         # Lista os gastos
#         gastos = listar_gastos()
#         return render_template('gastos.html', gastos=gastos)  # Renderiza a lista de gastos

#     @staticmethod
#     def update_gasto(gasto_id,data,valor,categoria_nome):
#         if data is not None and valor is not None and categoria_nome is not None:
#             # Atualiza o gasto
#             atualizar_gasto(gasto_id, data, valor, categoria_nome)
#             return redirect('/gastos')  # Redireciona para a lista de gastos
#         # gasto = listar_gastos(gasto_id)  # Busca o gasto específico para exibição no formulário de edição
#         return render_template('updateGasto.html', gasto_id=gasto_id)  # Renderiza o formulário de edição

#     @staticmethod
#     def delete_gasto(gasto_id):
#         # Deleta o gasto
#         resultado = deletar_gasto(gasto_id)
#         return redirect('/gastos')  # Redireciona para a lista de gastos       #ver
