import datetime
import boto3

# Configuração do cliente boto3
ce_client = boto3.client('ce', region_name='us-east-1')  # Substitua 'us-east-1' pela sua região

# Taxa de câmbio da AWS para converter para BRL
CURRENCY_CONVERSION_RATE = 5.50  # Substitua pelo valor da taxa de câmbio atual

# Função para obter o período desejado de forma interativa
def get_custom_date_range():
    """
    Obtém o período desejado de forma interativa.
    """
    print("Digite o período desejado para análise de custos:")
    start_date_str = input("Data de início (AAAA-MM-DD): ")
    end_date_str = input("Data de término (AAAA-MM-DD): ")

    try:
        start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
        return start_date, end_date
    except ValueError:
        print("Formato de data inválido. Use o formato AAAA-MM-DD.")
        return get_custom_date_range()

# Função para obter e listar os serviços e valores de gastos
def list_costs_by_service(start_date, end_date):
    """
    Obtém e lista os serviços e valores de gastos.
    """
    response = ce_client.get_cost_and_usage(
        TimePeriod={
            'Start': start_date.strftime('%Y-%m-%d'),
            'End': end_date.strftime('%Y-%m-%d')
        },
        Granularity='MONTHLY',
        Metrics=['BlendedCost'],  # Pode adicionar outras métricas, se desejar
        GroupBy=[
            {
                'Type': 'DIMENSION',
                'Key': 'SERVICE'
            }
        ]
    )

    for result in response['ResultsByTime']:
        for group in result['Groups']:
            service_name = group['Keys'][0]
            cost = float(group['Metrics']['BlendedCost']['Amount'])
            cost_brl = cost * CURRENCY_CONVERSION_RATE
            print(f"Serviço: {service_name}, Custo em USD: ${cost:.2f}, Custo em BRL: R${cost_brl:.2f}")

if __name__ == '__main__':
    start_date, end_date = get_custom_date_range()
    list_costs_by_service(start_date, end_date)
