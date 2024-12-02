from flask import render_template, request, redirect
from app.Model.limitesModel import DataDeExpiracaoInvalida, LimiteGastosDB, LimiteGastos, ValorInsulficiente
from app.Model.dateUtil import converte_para_date

class ExisteLimiteEmAndamento(Exception):
    pass

class LimitesController:

    @staticmethod
    def add_limite(CPF):
        if LimitesController.limite_ja_existe(CPF):
            raise ExisteLimiteEmAndamento("Já existe um limite em andamento")
        valor, data_expiracao = LimitesController.converte_input()
        limite_gastos = LimiteGastos(valor, data_expiracao)
        limite_db = LimiteGastosDB()
        limite_db.registrar_limite_com_transacao(limite_gastos, CPF)
        return redirect("/limites-gastos")

    def get_limites(CPF, erros):
        limites_db = LimiteGastosDB()
        limites = limites_db.resgatar_limites(CPF) or []
        
        return render_template("limites.html", limites=limites, erros = erros)
    
    def get_limite(limite_id):
        limites_db = LimiteGastosDB()
        limite = limites_db.resgatar_limite(limite_id)
        return limite
    
    def deletar_limite(limite_id):
        limite_db = LimiteGastosDB()
        limite_db.deletar_limite(limite_id)
        return redirect("/limites-gastos")
    
    def editar_limite(limite_id):
        limites_db = LimiteGastosDB()
        valor, data_expiracao = LimitesController.converte_input()
        limite = LimiteGastos(valor, data_expiracao, id=limite_id)
        limites_db.atualizar_limite(limite)
        return redirect("/limites-gastos")        
        
    def converte_input():
        try:
            valor = int(request.form.get("valor"))
        except ValueError:
            raise ValorInsulficiente("O valor inserido para o limite deve ser maior que 0")
        try:
            data_expiracao = converte_para_date(request.form.get("data_expiracao"))
        except ValueError:
            raise DataDeExpiracaoInvalida("Só é possível definir o vencimento do limite para datas futuras")
        return valor, data_expiracao

    def limite_ja_existe(CPF):
        limites_db = LimiteGastosDB()
        limites = limites_db.resgatar_limites(CPF)
        for limite in limites:
            if limite.valido == 1:
                return True
        return False
        