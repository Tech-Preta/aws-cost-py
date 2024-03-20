import unittest
from analise_de_custos import get_custom_date_range, list_costs_by_service
class TestAnaliseDeCustos(unittest.TestCase):

    def test_get_custom_date_range_valid_input(self):
        start_date, end_date = get_custom_date_range()
