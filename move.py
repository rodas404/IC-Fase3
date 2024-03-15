# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 16:40:28 2023

@author: footr
"""

import os
import shutil

# Caminho para a pasta de origem
pasta_origem = "dataset/pendentes/test/metal"

# Caminho para a pasta de destino
pasta_destino = "dataset/test/metal"

# Número de imagens a serem movidas
numero_de_imagens = 700  



# Lista todos os arquivos na pasta de origem
arquivos = os.listdir(pasta_origem)

# Seleciona os primeiros x arquivos
arquivos_selecionados = arquivos[:numero_de_imagens]
#arquivos_selecionados = arquivos[-numero_de_imagens:]

# Move os arquivos para a pasta de destino
for arquivo in arquivos_selecionados:
    caminho_origem = os.path.join(pasta_origem, arquivo)
    caminho_destino = os.path.join(pasta_destino, arquivo)
    shutil.move(caminho_origem, caminho_destino)

print(f"{numero_de_imagens} imagens movidas de {pasta_origem} para {pasta_destino}.")
