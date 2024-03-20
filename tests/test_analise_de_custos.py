"""
Este é o módulo de teste para o módulo analise_de_custos.
Ele contém testes unitários para as funções get_custom_date_range e list_costs_by_service.
"""

import unittest
from analise_de_custos import get_custom_date_range

class TestAnaliseDeCustos(unittest.TestCase):
    """
    Esta classe contém testes unitários para o módulo analise_de_custos.
    """

    def test_get_custom_date_range_valid_input(self):
        """
        Testa a função get_custom_date_range com uma entrada válida.
        """
        input_start_date, input_end_date = get_custom_date_range()
