from API_Data.get_bookings_description import get_booking_updates
from Database.database import get_db,Base,engine
from Database.commit_to_db import commit_data_on_db
from Logs.send_email import email_credenciais,email

def main():
    # Cria as tabelas no banco de dados, se ainda não existirem
    Base.metadata.create_all(engine)
    
    # Armazena as reservas no banco de dados
    commit_data_on_db(bookings=get_booking_updates(), db=get_db())

    except Exception as e:

        email(credenciais=email_credenciais(),erro=e)

if __name__ == "__main__":
    main()