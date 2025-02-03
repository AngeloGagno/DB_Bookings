from API_Data.get_bookings_description import get_bookings_description
from Database.database import get_db,Base,engine
from Database.commit_to_db import commit_data_on_db
from datetime import datetime,timedelta
from Logs.send_email import email_credenciais,email

def main(start_date=None, end_date=None):
    """
    Função principal para buscar reservas e armazená-las no banco de dados.
    """
    # Status predefinidos para as reservas
    Status = ['CONFIRMED', 'PAID', 'OWNER', 'UNAVAILABLE', 'UNPAID','CANCELLED']
    
    # Busca as reservas da API

    data = get_bookings_description(date_begin=start_date, date_end=end_date, status=Status)
    print(data)
    # Cria as tabelas no banco de dados, se ainda não existirem
    Base.metadata.create_all(engine)
        
    # Armazena as reservas no banco de dados
    commit_data_on_db(bookings=data, db=get_db())

    
if __name__ == "__main__":
    now = datetime.now()
    day =  now - timedelta(days=1)
    main(start_date=day.strftime("%Y-%m-%d"), end_date=now.strftime("%Y-%m-%d"))
