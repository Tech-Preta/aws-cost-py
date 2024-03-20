from analise_de_custos import get_custom_date_range, list_costs_by_service

def main():
    start_date, end_date = get_custom_date_range()
    if start_date and end_date:
        list_costs_by_service(start_date, end_date)

if __name__ == '__main__':
    main()
