# conversor_de_moedas

Aplicação Python para obter e converter cotações do dólar em relação ao real (USD/BRL). Inclui funcionalidades para buscar a cotação do dólar para uma data específica, converter valores e salvar as informações em um arquivo CSV. Utiliza requests para requisições HTTP, pandas para manipulação de dados e logging para registro de eventos.

## Funcionalidades

- **Obtenção da cotação atual do dólar**: Funções para buscar a cotação atual do dólar em relação ao real (USD/BRL).
- **Obtenção da cotação do dólar para uma data específica**: Funções para buscar a cotação do dólar em uma data específica (requer chave de acesso).
- **Conversão de valores**: Ferramentas para converter valores de dólar para real utilizando a cotação obtida.
- **Salvamento de dados em CSV**: Funções para salvar as cotações do dólar em um arquivo CSV utilizando pandas.
- **Tratamento de logs**: Utiliza a biblioteca logging para registrar eventos e erros.

## Estrutura do Repositório

```plaintext
conversor_de_moedas/
├── LICENSE
├── README.md
├── gitignore
├── env
├── env_exemplo
├── dados
│   └── csv
│       └── taxas.csv
├── requirements.txt
├── src
│   ├── api_client.py
│   ├── app.log
│   ├── config.py
│   └── main.py
└── tests
    └── test_api_client.py
```

## Como Usar

1. Clone o repositório:
    ```bash
    git clone https://github.com/kleiton/conversor_de_moedas.git
    cd conversor_de_moedas
    ```

2. Instale as dependências:
    - Certifique-se de ter o Python instalado.
    - Instale as bibliotecas necessárias:
    ```bash
    pip install -r requirements.txt
    ```

3. Crie um arquivo `.env` na raiz do projeto e adicione sua chave de acesso:
    - Use o arquivo `.env_exemplo` como referência.
    ```plaintext
    API_KEY=YOUR_ACCESS_KEY
    ```

4. Execute o programa:
    ```bash
    python src/main.py
    ```

5. Execute os testes:
    ```bash
    python -m unittest discover -s tests
    ```


## Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request para melhorias.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.