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

#salvar em planilha Excel
def salvar_em_excel(df):
    df.to_excel("cadastro_clientes.xlsx", index = false)
    print("Dados salvos em cadastro_clientes.xlsx")

#Exemplo de uso
if __name__ == "__main__":
    connection = conectar_bd()
    if connection:
        criar_tabela_veiculos(connection)
        inserir_veiculo(connection, "Tiguain", 2020, 65000.00)
        inserir_veiculo(connection, "T-Cross", 2023, 95000.00)
        inserir_veiculo(connection, "UP TSI250", 2019, 55000.00)
        inserir_veiculo(connection, "Polo", 2015, 35000.00)
        inserir_veiculo(connection, "Gol Plus", 2010, 15000.00)
        inserir_veiculo(connection, "Uno Way", 2014, 40000.00)
        inserir_veiculo(connection, "Pulse", 2023, 105000.00)
        inserir_veiculo(connection, "Toro", 2021, 135000.00)
        inserir_veiculo(connection, "Argo", 2022, 80000.00)
        inserir_veiculo(connection, "Palio", 2014, 18900.00)
        inserir_veiculo(connection, "Maverick", 2024, 250000.00)
        inserir_veiculo(connection, "Ranger Raptor", 2023, 180000.00)
        inserir_veiculo(connection, "Ford Ka", 2018, 33000.00)
        inserir_veiculo(connection, "Fiesta", 2012, 25000.00)
        inserir_veiculo(connection, "Fusion", 2021, 75000.00)
        inserir_veiculo(connection, "Onix", 2015, 17900.00)
        inserir_veiculo(connection, "Blazer", 2022, 120000.00)
        inserir_veiculo(connection, "Equinox", 2011, 200000.00)
        inserir_veiculo(connection, "Corsa Milenium", 2011, 13000.00)

        nome_veiculo = input("Digite o nome do veículo: ")
        preco_veiculo = input("Digite o preço do veículo: ")
        parcelas = int(input("Digite o número de parcelas desejados: "))

        entrada, valor_parcela = calcular_financiamento(preco_veiculo, parcelas)
        print(f"Entrada: R%{entrada:.2f}")
        print(f"Valor da parcela: R${valor_parcela:.2f}")

        cliente = cadastrar_cliente()
        if cliente:
            df = pd.Dataframe([cliente], columns=["Nome", "Endereço", "CPF", "RG", "Renda"])
            salvar_em_excel(df)
        
        connection.close()





