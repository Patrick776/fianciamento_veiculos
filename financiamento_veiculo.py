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

#cálculo de financiamento
def calcular_financiamento(preco, parcelas):
    entrada = preco * 0.2
    juros = 0.03
    valor_parcela = (preco - entrada) * (1 + juros) / parcelas
    return entrada, valor_parcela

#cadastro de cliente
def cadastrar_cliente():
    nome = input("Nome completo: ")
    endereco = input("Endereço: ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    empregado = input("Empregado (S/N): ").upper()
    if empregado == "N":
        print("Proposta recusada para clientes desempregados.")
        return None
    else:
        renda = float(input("Renda mensal: "))
        return nome, endereco, cpf, rg, renda





