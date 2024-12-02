from app.Model.databaseManager import DBTransactionManager, BaseDB
from datetime import date
from app.Model.dateUtil import converte_para_date

class ValorInsulficiente(Exception):
    pass

class DataDeExpiracaoInvalida(Exception):
    pass

class LimiteGastos:
    def __init__(self, valor: float, data_expiracao: date, data_inicio: date = date.today(), id: int = None):
        if valor is not None and valor <= 0:
            raise ValorInsulficiente("O valor inserido para o limite deve ser maior que 0")
        elif data_expiracao < data_inicio:
            raise DataDeExpiracaoInvalida("Só é possível definir o vencimento do limite para datas futuras")
        
        self.valor = valor
        self.data_expiracao = data_expiracao
        self.data_inicio = data_inicio
        self.valido = int(data_expiracao >= date.today())
        self.id = id

        

class LimiteGastosDB:
    def __init__(self):
        self._db = BaseDB()

    def registrar_limite_com_transacao(self, limite_gastos: LimiteGastos, CPF):
        with DBTransactionManager() as db_manager:
            db_manager.executar_transacao(
                comando="INSERT INTO Limites (valor, data_expiracao, data_inicio, usuario_id) VALUES (?, ?, ?, ?)",
                params=(
                    limite_gastos.valor,
                    limite_gastos.data_expiracao,
                    limite_gastos.data_inicio,
                    CPF,
                ),
            )
            
    def resgatar_limites(self, CPF):
        limites = []
        with DBTransactionManager() as db_manager:
            resposta = db_manager.executar_transacao(
                comando="SELECT * FROM Limites WHERE usuario_id = ?",
                params= (CPF,),   
            )
            limites = [
                LimiteGastos(
                    id=int(row[0]) , 
                    valor=float(row[1]), 
                    data_expiracao=converte_para_date(row[2]), 
                    data_inicio=converte_para_date(row[3]),
                    ) for row in resposta
                ]
        return limites
    
    def resgatar_limite(self, limite_id:int):
        limite = None
        with DBTransactionManager() as db_manager:
            resposta = db_manager.executar_transacao(
                comando="SELECT * FROM Limites WHERE id = ?",
                params= (limite_id,),   
                fetchone=True
            )
            limite = LimiteGastos(
                id=int(resposta[0]) , 
                valor=float(resposta[1]), 
                data_expiracao=converte_para_date(resposta[2]), 
                data_inicio=converte_para_date(resposta[3]),
            )
        return limite

    def deletar_limite(self, limite_id):
        with DBTransactionManager() as db_manager:
            db_manager.executar_transacao(
                comando="DELETE FROM Limites WHERE id = ?",
                params=(limite_id,),
            )
            
    def atualizar_limite(self, limite_gastos: LimiteGastos):
        with DBTransactionManager() as db_manager:
            db_manager.executar_transacao(
                comando="UPDATE Limites SET (valor, data_expiracao) = (?, ?) WHERE id = ?",
                params=(limite_gastos.valor, limite_gastos.data_expiracao, limite_gastos.id)
            )
            
