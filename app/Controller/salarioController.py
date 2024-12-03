# app/controllers/categoriasController.py
from flask import render_template, request, redirect, flash

class SalarioController:
    horas = 1
    salario = 1
    @staticmethod
    def get_salario():
        return render_template('salario.html', salario = SalarioController.salario, horas_trabalho = SalarioController.horas)

    @staticmethod
    def add_salario():
        novo_salario = request.form.get('salario', type = float)
        novas_horas = request.form.get('horas_trabalho', type = float)

        if novo_salario <= 0 or novas_horas <= 0:
            flash('Salário e horas de trabalho devem ser positivos!')
            return redirect('/salario')
        else:
            SalarioController.salario = novo_salario
            SalarioController.horas = novas_horas
            flash('Salário e horas de trabalho atualizados com sucesso!')
            return redirect('/salario')
        
    @staticmethod
    def get_salario_hora():
        return SalarioController.salario/SalarioController.horas