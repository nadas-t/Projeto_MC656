from app.Model.configBancoModel import InstanciadorDB


def Cria():
    instanciador_db = InstanciadorDB()
    instanciador_db.CriarBancoDados()
