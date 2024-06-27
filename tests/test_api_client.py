import unittest
from unittest.mock import patch
from api_client import ClienteMoeda

class TestClienteMoeda(unittest.TestCase):

    @patch('api_client.requests.get')
    def test_obter_taxa_cambio_sucesso(self, mock_get):
        mock_response = {
            "rates": {
                "BRL": 5.25
            }
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        cliente = ClienteMoeda()
        taxa = cliente.obter_taxa_cambio()
        self.assertEqual(taxa, 5.25)

    @patch('api_client.requests.get')
    def test_obter_taxa_cambio_falha(self, mock_get):
        mock_get.return_value.status_code = 404

        cliente = ClienteMoeda()
        with self.assertRaises(Exception):
            cliente.obter_taxa_cambio()

    @patch('api_client.requests.get')
    def test_obter_taxa_para_data_sucesso(self, mock_get):
        mock_response = {
            "rates": {
                "BRL": 5.20
            }
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        cliente = ClienteMoeda()
        taxa = cliente.obter_taxa_para_data("2023-01-01")
        self.assertEqual(taxa, 5.20)

if __name__ == '__main__':
    unittest.main()