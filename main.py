import csv
import os
from datetime import datetime, timedelta

# Nome do arquivo CSV
arquivo_csv = 'gastos.csv'

# Função para garantir que o arquivo CSV seja criado com cabeçalhos, se ainda não existir
def criar_arquivo_csv():
    if not os.path.exists(arquivo_csv):
        with open(arquivo_csv, 'w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            escritor.writerow(['Data', 'Tipo de Gasto', 'Valor (R$)'])  # Cabeçalhos bem definidos

# Função para registrar o gasto
def registrar_gasto():
    # Perguntar a data, tipo de gasto e valor
    data = input("Digite a data do gasto (dd/mm/aaaa): ").strip()
    try:
        datetime.strptime(data, "%d/%m/%Y")  # Validando o formato da data
    except ValueError:
        print("Formato de data inválido. Tente novamente.")
        return
    
    tipo_gasto = input("Digite o tipo de gasto (ex: alimentação, transporte): ").strip()
    valor = input("Digite o valor do gasto: ").strip()

    try:
        valor = float(valor.replace(',', '.'))  # Substituindo vírgula por ponto e validando o valor
    except ValueError:
        print("Valor inválido. Tente novamente.")
        return

    # Gravar os dados em um arquivo CSV
    with open(arquivo_csv, 'a', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        escritor.writerow([data, tipo_gasto, f"{valor:.2f}"])  # Formatação adequada de valores

    print(f"Gasto registrado: {data} - {tipo_gasto} - R$ {valor:.2f}")

# Função para exibir os gastos registrados
def exibir_gastos():
    try:
        with open(arquivo_csv, newline='', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo, delimiter=';')
            next(leitor)  # Pular os cabeçalhos
            print("\nGastos registrados:")
            encontrou_gastos = False
            for linha in leitor:
                print(f"Data: {linha[0]} | Tipo: {linha[1]} | Valor: R$ {linha[2]}")
                encontrou_gastos = True
            if not encontrou_gastos:
                print("Nenhum gasto registrado ainda.")
    except FileNotFoundError:
        print("Nenhum gasto registrado ainda.")

# Função para calcular o total de gastos em uma semana
def calcular_gasto_semanal():
    total = 0.0
    data_atual = datetime.now()
    data_inicio_semana = data_atual - timedelta(days=7)
    
    try:
        with open(arquivo_csv, newline='', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo, delimiter=';')
            next(leitor)  # Pular os cabeçalhos
            
            for linha in leitor:
                data_gasto = datetime.strptime(linha[0], "%d/%m/%Y")
                if data_inicio_semana <= data_gasto <= data_atual:
                    total += float(linha[2].replace(',', '.'))
                    
        # Registra o total da semana
        with open(arquivo_csv, 'a', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            escritor.writerow([data_atual.strftime("%d/%m/%Y"), 'Total da Semana', f"{total:.2f}"])
            
        print(f"Total de gastos na última semana: R$ {total:.2f}")
    except FileNotFoundError:
        print("Nenhum gasto registrado ainda.")

# Função para calcular o total de gastos em um mês
def calcular_gasto_mensal():
    total = 0.0
    data_atual = datetime.now()
    data_inicio_mes = data_atual - timedelta(days=30)
    
    try:
        with open(arquivo_csv, newline='', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo, delimiter=';')
            next(leitor)  # Pular os cabeçalhos
            
            for linha in leitor:
                data_gasto = datetime.strptime(linha[0], "%d/%m/%Y")
                if data_inicio_mes <= data_gasto <= data_atual:
                    total += float(linha[2].replace(',', '.'))
                    
        # Registra o total do mês
        with open(arquivo_csv, 'a', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            escritor.writerow([data_atual.strftime("%d/%m/%Y"), 'Total do Mês', f"{total:.2f}"])
            
        print(f"Total de gastos no último mês: R$ {total:.2f}")
    except FileNotFoundError:
        print("Nenhum gasto registrado ainda.")

# Criar o arquivo CSV se não existir
criar_arquivo_csv()

# Loop principal
while True:
    print("\n1. Registrar novo gasto")
    print("2. Exibir todos os gastos")
    print("3. Calcular gastos semanais")
    print("4. Calcular gastos mensais")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        registrar_gasto()
    elif opcao == '2':
        exibir_gastos()
    elif opcao == '3':
        calcular_gasto_semanal()
    elif opcao == '4':
        calcular_gasto_mensal()
    elif opcao == '5':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

