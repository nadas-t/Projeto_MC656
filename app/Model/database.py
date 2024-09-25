import sqlite3
import os

def conexao():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, '../database', 'database.db')
    con = sqlite3.connect(DB_PATH)
    return con
