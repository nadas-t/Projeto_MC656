from abc import ABC, abstractmethod
from app.Model.limitesModel import LimiteGastos, LimiteGastosDB

class NenhumLimiteCadastrado(Exception):
    pass

from abc import ABC, abstractmethod


class AlertaGastos(ABC):
    @property
    @abstractmethod
    def severidade(self):
        """ Propriedade correspondente ao nível do alerta,
        deve ser definida nas classes concretas"""
    
    @abstractmethod
    def exibir(self):
        """ Método abstrato para exibição de mensagem de alerta,
        deve ser implementado pelas classes concretas. """
        
class GeradorAlertaGastos(ABC):
    def __init__(self):
        self.alerta = self.factory_method()
    
    @abstractmethod
    def factory_method(self) -> AlertaGastos:
        pass
    
    def exibir_mensagem(self) -> str:
        return self.alerta.exibir()
    
    def exibir_severidade(self) -> str:
        return self.alerta.severidade

class GeradorAlertaGastosGrave(GeradorAlertaGastos):
    def factory_method(self):
        return AlertaGastosGrave()
    
class AlertaGastosGrave(AlertaGastos):
    @property
    def severidade(self):
        return "Grave"
    
    def exibir(self):
        return "Você excedou seu limite de gastos! Tenha cuidado com suas despesas!"
    
class GeradorAlertaGastosMedio(GeradorAlertaGastos):
    def factory_method(self):
        return AlertaGastosMedio()
    
class AlertaGastosMedio(AlertaGastos):
    @property
    def severidade(self):
        return "Média"
    
    def exibir(self):
        return "Você já atingiu 80% do seu limite de gastos! Fique de olho nas suas despesas!"
    
class GeradorAlertaGastosBaixo(GeradorAlertaGastos):
    def factory_method(self):
        return AlertaGastosBaixo()

class AlertaGastosBaixo(AlertaGastos):
    @property
    def severidade(self):
        return "Baixa"
    
    def exibir(self):
        return "Você já atingiu 50% do seu limite de gastos!"


# TODO pensar no que fazer para o caso em que não há alerta    

class MonitoramentoLimiteGastos:
    def __init__(self, CPF):
        self.limite = self.limite_atual(CPF)
        
    def atualizar_limite(self, CPF):
        self.limite = self.limite_atual
        
    def limite_atual(self, CPF):
        limite_db = LimiteGastosDB()
        limites = limite_db.resgatar_limites(CPF)
        for limite in limites:
            if limite.valido == 1:
                return limite
        return None
    
    def percentual_do_limite_excedido(self, total_gasto: float):
        return  total_gasto/self.limite

            
    def gerar_alerta(self, total_gasto):
        percentual = self.percentual_do_limite_excedido(total_gasto)
        if percentual >= 1:
            return GeradorAlertaGastosGrave()
        elif 0.8 <= percentual < 1:
            return GeradorAlertaGastosMedio()
        elif 0.5 <= percentual < 0.8: 
            return GeradorAlertaGastosBaixo()
        else:
            ...