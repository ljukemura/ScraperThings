# api_utils.py
import requests
import json
from datetime import datetime
import logging

def buscar_dados_api(url: str, headers: dict) -> dict:
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        logging.info(f"Resposta recebida com sucesso da URL: {url}")
        return json.loads(response.text)
    except requests.RequestException as e:
        logging.error(f"Erro ao buscar dados da API: {e}")
        return None 

def salvar_dados_json(dados: dict, caminho_base: str, nome_arquivo: str) -> None:
    if dados:
        data_atual = datetime.now().strftime("%Y_%m_%d")
        caminho_completo = f"{caminho_base}{nome_arquivo}_{data_atual}.json"
        try:
            with open(caminho_completo, 'w', encoding='utf-8') as arquivo_json:
                json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
            logging.info(f"Arquivo JSON '{caminho_completo}' foi salvo com sucesso.")
            return dados
        except IOError as e:
            logging.error(f"Erro ao escrever o arquivo: {e}")
    else:
        logging.warning("Nenhum dado para salvar.")

if __name__ == "__main__":
    #testes aqui
    print('testar')
