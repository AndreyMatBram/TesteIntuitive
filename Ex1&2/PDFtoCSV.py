import pdfplumber
import pandas as pd

# em meu primeiro codigo percebi que o pdfplumber tinha dificuldades de reconhecer as linhas da tabela ao pesquisar descobri
# que ele trabalha celula a celula e por isso transformava celular com multiplas linhas em 2 linhas na tabela
# para resolver isso fiz uma função que processa a tabela manualmente, procurando por quebras de linha e unindo as celulas
# ja aproveitei essa função para corrigir os nomes das celulas conforme solicitado, dentro do mesmo "for" para economizar processamento


def pdf_para_csv(arquivo_pdf, arquivo_csv):
    with pdfplumber.open(arquivo_pdf) as pdf:
        todas_tabelas = []
        for pagina in pdf.pages:
            tabelas = pagina.extract_tables()

            if tabelas:
                for tabela in tabelas:
                    # Processa a tabela manualmente
                    tabela_corrigida = []
                    for linha in tabela:
                        linha_corrigida = []
                        for celula in linha:
                            # Junta células de múltiplas linhas e corrige os nomes
                            if isinstance(celula, str):
                                celula = celula.replace("AMB", "Seg. Ambulatorial")
                                celula = celula.replace("OD", "Seg. Odontológica")
                                linha_corrigida.append(celula.replace("\n", " "))
                            else:
                                linha_corrigida.append("")
                        tabela_corrigida.append(linha_corrigida)
                    
                    df = pd.DataFrame(tabela_corrigida)
                    todas_tabelas.append(df)
    

    tabela_final = pd.concat(todas_tabelas, ignore_index=True)

    tabela_final = tabela_final.astype(str).drop_duplicates(keep='first')

    # Define a primeira linha como cabeçalho
    tabela_final.columns = tabela_final.iloc[0]
    tabela_final = tabela_final[1:]


    tabela_final.reset_index(drop=True, inplace=True)
 
    tabela_final.to_csv(arquivo_csv, index=False)

    
    print(f"Arquivo CSV salvo como: {arquivo_csv}")

arquivo_pdf = "./Ex1&2/Anexos/anexo1.pdf"
arquivo_csv = "Tabela.csv"
pdf_para_csv(arquivo_pdf, arquivo_csv)
