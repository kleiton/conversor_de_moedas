from api_client import ClienteMoeda
from datetime import datetime
import logging

def main():
    """
    Função principal para demonstrar o uso das funcionalidades da classe ClienteMoeda.

    Exemplos:
    - Obtém a taxa de câmbio atual.
    - Obtém a taxa de câmbio para uma data específica.
    - Obtém a taxa de câmbio do dia corrente.
    - Converte um valor em dólares para reais.
    - Salva dados de taxas de câmbio em um arquivo CSV.
    """
    logging.basicConfig(level=logging.INFO)
    cliente = ClienteMoeda()
    
    # Obter taxa de câmbio atual
    taxa = cliente.obter_taxa_cambio()
    if taxa:
        print(f"A taxa de câmbio USD/BRL é: {taxa}")
    
    # Obter taxa de câmbio para uma data específica
    data = "2023-01-01"
    taxa_para_data = cliente.obter_taxa_para_data(data)
    if taxa_para_data:
        print(f"A taxa de câmbio em {data} USD/BRL é: {taxa_para_data}")
    
    # Obter taxa de câmbio do dia corrente
    taxa_corrente = cliente.obter_taxa_cambio_corrente()
    if taxa_corrente:
        print(f"A taxa de câmbio USD/BRL para o dia corrente é: {taxa_corrente}")
    
    # Converter valor
    valor_usd = 100
    if taxa:
        valor_convertido = cliente.converter_valor(valor_usd, taxa)
        print(f"{valor_usd} USD é igual a {valor_convertido} BRL")
    
    # Preparar dados para salvar
    dados_taxas = []
    if taxa:
        dados_taxas.append({"data": datetime.now().strftime('%d/%m/%Y'), "valor_usd": 1, "valor_brl": cliente.converter_valor(1, taxa)})
    
    if taxa_para_data:
        dados_taxas.append({"data": "2023-01-01", "valor_usd": 1, "valor_brl": cliente.converter_valor(1, taxa_para_data)})
    else:
        print("Não foi possível obter a taxa de câmbio para a data 2023-01-01.")
    
    taxa_para_data2 = cliente.obter_taxa_para_data("2023-01-02")
    if taxa_para_data2:
        dados_taxas.append({"data": "2023-01-02", "valor_usd": 1, "valor_brl": cliente.converter_valor(1, taxa_para_data2)})
    else:
        print("Não foi possível obter a taxa de câmbio para a data 2023-01-02.")
    
    # Salvar dados de taxas em CSV
    if dados_taxas:
        logging.info("Dados preparados para salvar: %s", dados_taxas)
        cliente.salvar_taxas_csv(dados_taxas)

if __name__ == "__main__":
    main()