import pandas as pd

def verificar_duplicatas_individual(csv_path):
    df = pd.read_csv(csv_path, delimiter=';')
    resultado_duplicatas = {}
    for coluna in df.columns:  # Itera por todas as colunas
        duplicatas = df[coluna].duplicated(keep=False).any()
        resultado_duplicatas[coluna] = "Sim" if duplicatas else "Não"
    return resultado_duplicatas

def verificar_duplicatas_inter_tabelas(csv_paths):
    dataframes = []
    for path in csv_paths:
        df = pd.read_csv(path, delimiter=';')
        df['Tabela_Origem'] = path.split('/')[-1]
        dataframes.append(df)
    concat_df = pd.concat(dataframes)
    resultado_duplicatas = {}
    for coluna in concat_df.columns:
        duplicatas = concat_df[coluna].duplicated(keep=False).any()
        resultado_duplicatas[coluna] = "Sim" if duplicatas else "Não"
    return resultado_duplicatas

# Defina manualmente os caminhos dos arquivos CSV
csv_files = [
    '1T2023.csv',
    '1T2024.csv',
    '2T2023.csv',
    '2T2024.csv', 
    '3T2023.csv',
    '3T2024.csv',
    '4T2023.csv',
    '4T2024.csv']

# csv_files = [
#     'Relatorio_cadop.csv'
# ]

print("Duplicatas em tabelas individuais:")
for file in csv_files:
    duplicatas_individual = verificar_duplicatas_individual(file)
    print(f"Tabela {file}:")
    for coluna, resultado in duplicatas_individual.items():
        print(f" - Coluna '{coluna}': {resultado}")

if len(csv_files) > 1:
    print("\nDuplicatas entre tabelas:")
    duplicatas_inter_tabelas = verificar_duplicatas_inter_tabelas(csv_files)
    for coluna, resultado in duplicatas_inter_tabelas.items():
        print(f" - Coluna '{coluna}': {resultado}")
else:
    print("\nDuplicatas entre tabelas não aplicável (apenas uma tabela fornecida).")
