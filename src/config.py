from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
API_KEY = os.getenv("API_KEY")  # Obtém a chave de acesso da variável de ambiente