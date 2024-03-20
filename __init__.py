"""
Este é o módulo principal do projeto aws_cost_py.
Ele importa e executa as funções do módulo analise_de_custos.
"""

from .analise_de_custos import get_custom_date_range, list_costs_by_service

def main():
    """
    Função principal que solicita ao usuário um intervalo de datas e lista os custos dos serviços AWS para esse intervalo.
    """
    start_date, end_date = get_custom_date_range()
    list_costs_by_service(start_date, end_date)

if __name__ == "__main__":
    main()