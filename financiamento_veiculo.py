import mysql.connector
import pandas as pd

#conexão com o banco de dados
def conectar_bd():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passord = " ",
            database = "financiamento_veiculo"

        )

        return connection
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

#criação da tabela de veículos
def criar_tabela_veiculos(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            create table if not exists veiculos (
                id int auto_increment primary key,
                nome varchar(255) not null,
                ano int not null,
                preço decimal (10, 2) not null
                )
        """)
        connection.commit()
        print("Tabela de veículos criada com sucesso!")
    except mysql.connector.Error as e:
        print(f"Erro ao criar tabela de veículos: {e}")

#inserção de veículo
def inserir_veiculo(connection, nome, ano, preco):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            insert into veiculos (nome, ano, preco)
            values (%s, %s, %s)
            """, (nome,ano,preco))
            connection.commit()
            print("Veículo inserido com sucesso!")
    except mysql.connector.Error as e:
        print(f"Erro ao inserir veículo: {e}")



