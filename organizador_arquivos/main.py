import os
import shutil

# Criar um mapeamento de tipos e pastas
pastas_e_extensoes = {
    "Documentos": [".txt", ".docx", ".pdf"],
    "Imagens": [".png",".jpg","jpeg"],
    "Planilhas": [".xlsx"],
}

# Informar a pasta e gerar uma lista com os arquivos
pasta_atual = "."
lista_de_arquivos = os.listdir(pasta_atual)

# Criar um loop iterando por cada arquivo
for arquivo in lista_de_arquivos:
    nome, extensao = os.path.splitext(arquivo)

# Identificar a pasta do arquivo por extensão
    # Iterar cada chave do dicionário
    for chave in pastas_e_extensoes:

# Verificar se extensão do arquivo está na lista de arquivos
        lista_de_valores = pastas_e_extensoes[chave]
        if extensao in lista_de_valores:
            # Mover o arquivo para a pasta definida
            if not os.path.exists(chave):
                os.mkdir(chave)
            
            origem = os.path.join(pasta_atual, arquivo)
            destino = os.path.join(pasta_atual, chave, arquivo)

            shutil.move(origem, destino)
            print("Arquivo movido com sucesso.")
                


