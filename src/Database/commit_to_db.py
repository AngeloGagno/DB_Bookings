from Database.models import BD_Bookings
from sqlalchemy.orm import Session

def commit_data_on_db(bookings,db:Session):
    for item in bookings:
        registros = BD_Bookings(
                id_booking = item['id_booking'],
                portal_reference=item['Portal Reference'],
                check_in_data = item['check_in_date'],
                check_out_data=item['check_out_date'],
                update_date=item['update_date'],
                reservation_date=item['reservation_date'],
                status=item['status'],
                accommodation_code=item['accommodation_code'],
                sale_channel=item['sale_channel'],
                total_payment=item['total_payment'],
                net_payment=item['net_payment'],
                extra_value=item['extras_value'],
                extra_descrition=item['extra_info'],
                portal_comission=item['portal_comission'],
        )
        db.merge(registros)
    db.commit()
    print("Dados inseridos com sucesso!")