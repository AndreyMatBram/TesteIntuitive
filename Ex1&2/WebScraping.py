import requests
import zipfile
import os

def BaixarEZipar(urls, nomes_arquivos, nome_zip):
    # Criar uma pasta temporária para armazenar os arquivos
    os.makedirs("temp", exist_ok=True)

    for url, nome_arquivo in zip(urls, nomes_arquivos):
        resposta = requests.get(url)
        with open(f"temp/{nome_arquivo}", "wb") as arquivo:
            arquivo.write(resposta.content)

    with zipfile.ZipFile(nome_zip, "w") as zipf:
        for nome_arquivo in nomes_arquivos:
            zipf.write(f"temp/{nome_arquivo}", arcname=nome_arquivo)

    # Remover os arquivos temporários
    for nome_arquivo in nomes_arquivos:
        os.remove(f"temp/{nome_arquivo}")
    os.rmdir("temp")

# URLs dos arquivos a serem baixados
urls = [
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",  
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
]


nomes_arquivos = ["anexo1.pdf", "anexo2.pdf"]
nome_zip = "Anexos.zip"

# Chamar a função
BaixarEZipar(urls, nomes_arquivos, nome_zip)

print(f"Arquivos salvos em {nome_zip}")
