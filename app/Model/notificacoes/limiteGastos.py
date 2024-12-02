from abc import ABC, abstractmethod


class CriadorAlertaGastos(ABC):
    
    @abstractmethod
    def factory_method(self):
        pass
    
class AlertaGastos(ABC):
    ...

class CriadorAlertaGastosGrave(CriadorAlertaGastos):
    def factory_method(self):
        return AlertaGastosGrave()
    
class AlertaGastosGrave(AlertaGastos):
    ...
    
class AlertaGastosMedio(AlertaGastos):
    ...

class AlertaGastosBaixo(AlertaGastos):
    ...