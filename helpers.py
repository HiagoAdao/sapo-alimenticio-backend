import os
import sqlite3

path = './filestxt'

def limpar_tabelas():
    try:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM core_alimento')
        cursor.execute('DELETE FROM core_arquivo')
        conn.commit()
        print('Limpeza das tabelas concluída.')
        conn.close()

    except:
        print('Não possivel conectar ao Banco de Dados')


def limpar_arquivos():
    dir = os.listdir(path)
    for file in dir:
        if '.txt' in file:
            os.remove(path+'/'+file)
    print('Arquivos excluidos')