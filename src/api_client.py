import requests
import logging
import pandas as pd
import os
from datetime import datetime
from config import API_URL, API_KEY

# Configuração do logger
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class ClienteMoeda:
    def __init__(self, api_url=API_URL, api_key=API_KEY):
        """
        Inicializa a classe ClienteMoeda.

        Parâmetros:
        - api_url (str): URL da API para obter as taxas de câmbio. Padrão é API_URL.
        - api_key (str): Chave de acesso para a API.
        """
        self.api_url = api_url
        self.api_key = api_key

    def obter_taxa_cambio(self, moeda_destino="BRL"):
        """
        Obtém a taxa de câmbio atual do dólar para a moeda especificada.

        Parâmetros:
        - moeda_destino (str): A moeda para a qual deseja obter a taxa de câmbio. Padrão é "BRL".

        Retorno:
        - float: A taxa de câmbio atual do dólar para a moeda especificada.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            dados = response.json()
            taxa = dados.get("rates", {}).get(moeda_destino, None)
            if taxa:
                logging.info(f"Taxa de câmbio obtida: 1 USD = {taxa} {moeda_destino}")
            else:
                logging.warning(f"Taxa de câmbio para {moeda_destino} não encontrada.")
            return taxa
        except requests.RequestException as e:
            logging.error(f"Erro ao obter taxa de câmbio: {e}")
            raise

    def obter_taxa_para_data(self, data, moeda_destino="BRL"):
        """
        Obtém a taxa de câmbio do dólar para uma data específica.

        Parâmetros:
        - data (str): A data no formato 'YYYY-MM-DD' para a qual deseja obter a taxa de câmbio.
        - moeda_destino (str): A moeda para a qual deseja obter a taxa de câmbio. Padrão é "BRL".

        Retorno:
        - float: A taxa de câmbio do dólar para a data e moeda especificadas.
        """
        try:
            url = f"https://api.exchangerate.host/{data}?access_key={self.api_key}"
            logging.info(f"Obtendo taxa de câmbio da URL: {url}")
            response = requests.get(url)
            response.raise_for_status()
            dados = response.json()
            logging.info(f"Resposta da API: {dados}")
            taxa = dados.get("rates", {}).get(moeda_destino, None)
            if taxa:
                logging.info(f"Taxa de câmbio em {data}: 1 USD = {taxa} {moeda_destino}")
            else:
                logging.warning(f"Taxa de câmbio para {moeda_destino} não encontrada em {data}.")
            return taxa
        except requests.RequestException as e:
            logging.error(f"Erro ao obter taxa de câmbio para {data}: {e}")
            return None

    def obter_taxa_cambio_corrente(self, moeda_destino="BRL"):
        """
        Obtém a taxa de câmbio do dólar para o dia corrente.

        Parâmetros:
        - moeda_destino (str): A moeda para a qual deseja obter a taxa de câmbio. Padrão é "BRL".

        Retorno:
        - float: A taxa de câmbio do dólar para o dia corrente.
        """
        data_corrente = datetime.now().strftime('%Y-%m-%d')
        return self.obter_taxa_para_data(data_corrente, moeda_destino)

    def converter_valor(self, valor_usd, taxa):
        """
        Converte um valor em dólares para a moeda especificada usando a taxa de câmbio fornecida.

        Parâmetros:
        - valor_usd (float): O valor em dólares a ser convertido.
        - taxa (float): A taxa de câmbio a ser utilizada para a conversão.

        Retorno:
        - float: O valor convertido na moeda especificada.
        """
        if taxa is None:
            raise ValueError("A taxa de câmbio fornecida é inválida (None).")
        valor_convertido = valor_usd * taxa
        logging.info(f"Valor convertido: {valor_usd} USD = {valor_convertido} BRL")
        return valor_convertido

    def salvar_taxas_csv(self, dados, arquivo="dados/csv/taxas.csv"):
        """
        Salva os dados de taxas de câmbio em um arquivo CSV.

        Parâmetros:
        - dados (list): Lista de dicionários contendo os dados a serem salvos.
        - arquivo (str): Nome do arquivo CSV onde os dados serão salvos. Padrão é "dados/csv/taxas.csv".

        Retorno:
        - None
        """
        # Garante que o diretório exista
        if not os.path.exists(os.path.dirname(arquivo)):
            os.makedirs(os.path.dirname(arquivo))
            logging.info(f"Diretório criado: {os.path.dirname(arquivo)}")
        
        logging.info(f"Salvando dados no arquivo: {arquivo}")
        df = pd.DataFrame(dados)
        df['data'] = pd.to_datetime(df['data'], dayfirst=True).dt.strftime('%d-%m-%Y')
        df.to_csv(arquivo, index=False)
        logging.info(f"Dados salvos no arquivo {arquivo}")