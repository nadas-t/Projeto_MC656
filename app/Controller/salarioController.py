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
        SalarioController.salario = request.form.get('salario', type = float)
        SalarioController.horas = request.form.get('horas_trabalho', type = float)
        flash('Salário e horas de trabalho atualizados com sucesso!')
        return redirect('/salario')
    
    @staticmethod
    def get_salario_hora():
        return SalarioController.salario/SalarioController.horas














