import os
from os import walk
import glob
import codecs
import re
from datetime import datetime
# from .models import Alimento, Arquivo
from django.db import connection, transaction


# import sqlite3

pathfiles = './filestxt'
mylines = []


def extrair_db():
    
    cursor = connection.cursor()

    def insert_data():

        try:
            # inserindo dados na tabela

            cursor.executemany("""INSERT INTO core_alimento (nome, quantidade, proteinas, carboidratos, gorduras, criado_em)
            VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT(nome) DO NOTHING """, mylines)

            # cursor.executemany("""
            # INSERT INTO core_alimento (nome, quantidade, proteinas, carboidratos, gorduras, criado_em)
            # VALUES (:nome, :quantidade, :proteinas, :carboidratos, :gorduras, :criado_em)
            # ON CONFLICT(nome) DO UPDATE SET nome=:nome, quantidade=:quantidade, proteinas=:proteinas, carboidratos=:carboidratos, gorduras=:gorduras
            # """, mylines)

            print('Dados inseridos com sucesso.')
        except:
            print('Ocorreu um erro ao inserir os dados no banco de dados')
        

    def read_file(file):
        count = 0
        with codecs.open(file, encoding='utf-8') as f:
            for line in f:        
                line = line.replace('\n','')
                line = re.split(r'\s\s+', line.capitalize())
                line.append(datetime.now())
                if count > 1:
                    mylines.append(line)
                count += 1
            f.close()

        insert_data()
        mylines.clear()
        

    def find_files(path):

        for (dirpath, dirnames, filenames) in walk(path):
            for file in filenames:
                if '.txt' in file:
                    read_file(path+'/'+file)
                    # print(path+'/'+file)


    find_files(pathfiles)

    cursor.close()


# extrair_db()