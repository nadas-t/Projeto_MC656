from app.Model.monitoramento.limiteGastos import MonitoramentoLimiteGastos, GeradorAlertaGastos, NenhumLimiteCadastrado

class AlertasLimiteGastos:
    @staticmethod
    def capturar_alerta(CPF):
        try:
            monitor_limite = MonitoramentoLimiteGastos(CPF)
            alerta = monitor_limite.monitorar_limite()
            return formatar_alerta(alerta)
        except NenhumLimiteCadastrado:
            return None
    
def formatar_alerta(alerta: GeradorAlertaGastos):
    if alerta is not None:
        return {
            "severidade": alerta.exibir_severidade,
            "mensagem": alerta.exibir_mensagem(),
            "valor_limite": alerta.limite.valor,
            "total_gasto": alerta.total_gasto
        }
    return None
