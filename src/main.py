from API_Data.Get.get_bookings_description import get_bookings_description
from Database.database import get_db,Base,engine
from Database.commit_to_db import commit_data_on_db
import argparse

def main(start_date=None, end_date=None):
    """
    Função principal para buscar reservas e armazená-las no banco de dados.
    """
    # Status predefinidos para as reservas
    Status = ['CONFIRMED', 'PAID', 'OWNER', 'UNAVAILABLE', 'UNPAID']
    
    # Busca as reservas da API
    data = get_bookings_description(date_begin=start_date, date_end=end_date, status=Status)
    
    # Cria as tabelas no banco de dados, se ainda não existirem
    Base.metadata.create_all(engine)
    
    # Armazena as reservas no banco de dados
    commit_data_on_db(bookings=data, db=get_db())

if __name__ == "__main__":
    # Configuração do argparse para argumentos de linha de comando
    parser = argparse.ArgumentParser(description="Busca e armazena reservas de um período.")
    parser.add_argument(
        "--start_date",
        required=True,
        help="Data inicial no formato YYYY-MM-DD"
    )
    parser.add_argument(
        "--end_date",
        required=True,
        help="Data final no formato YYYY-MM-DD"
    )
    
    # Parse dos argumentos da linha de comando
    args = parser.parse_args()
    
    # Chama a função principal com os argumentos
    main(start_date=args.start_date, end_date=args.end_date)
