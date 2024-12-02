from datetime import datetime, date

def converte_para_date(data):
    if isinstance(data, str):
        return datetime.strptime(data, "%Y-%m-%d").date()
    if isinstance(date, data):
        return data
    raise Exception("Não foi possível converter para date uma variavel do tipo ", type(data))