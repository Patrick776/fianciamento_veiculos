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

