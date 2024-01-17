import _utils
import pandas as pd
from datetime import datetime
import numpy as np

# Parâmetros
url_api = r'https://api-middleware-mcd.mcdonaldscupones.com/api/restaurant/list'
headers_api = {
    'authority': 'api-middleware-mcd.mcdonaldscupones.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-none-match': 'W/"3f7568-AJdM0Gr2nRynl4WqrjfFvu2GyMY"',
    'origin': 'https://www.mcdonalds.com.br',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'x-app-country': 'BR',
}
caminho_raw = r'.\data\raw\id_01\\'
caminho_siver = r'.\data\silver\id_01\\'
nome_arquivo = 'mcdonalds'

# parte 1 - Extrair e salvar dados brutos (E - ETL / camada raw)
dados_api = _utils.buscar_dados_api(url_api, headers_api)
arquivo_raw = _utils.salvar_dados_json(dados_api, caminho_raw, nome_arquivo)

# parte 2 - Tranformar dados para utilização (T - ETL)
with open(arquivo_raw, 'r', encoding='utf-8') as file:
    data = pd.read_json(file)

df = pd.json_normalize(data['data'])

# parte 3 - Disponibilizar tabela trata (L - ETL / camada silver)
df.to_csv(f'{caminho_siver}{nome_arquivo}.csv', index=False)

df.head().to_csv(f'{caminho_siver}{nome_arquivo}_head.csv', index=False)


