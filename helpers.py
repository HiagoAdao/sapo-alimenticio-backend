import os
# import sqlite3
from django.db import connection, transaction


path = './filestxt'

def limpar_tabelas():
    try:
        cursor = connection.cursor()
        cursor.execute('TRUNCATE core_alimento, core_arquivo')
        print('Limpeza das tabelas concluída.')

    except:
        print('Não possivel conectar ao Banco de Dados')


def limpar_arquivos():
    try:
        dir = os.listdir(path)
        for file in dir:
            if '.txt' in file:
                os.remove(path+'/'+file)
        print('Arquivos excluidos')
    except:
        print('Não foi possível limpar os arquivos')
