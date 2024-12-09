from API_Data.get_bookings_description import get_booking_updates
from Database.database import get_db,Base,engine
from Database.commit_to_db import commit_data_on_db


def main():
    # Status predefinidos para as reservas
    Status = ['CONFIRMED', 'PAID', 'OWNER', 'UNAVAILABLE', 'UNPAID']
    
    # Busca as reservas da API
    data = get_booking_updates()
    
    # Cria as tabelas no banco de dados, se ainda não existirem
    Base.metadata.create_all(engine)
    
    # Armazena as reservas no banco de dados
    commit_data_on_db(bookings=data, db=get_db())

if __name__ == "__main__":
    main()