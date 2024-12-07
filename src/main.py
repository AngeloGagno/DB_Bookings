from API_Data.Get.get_bookings_description import get_bookings_description
from Database.database import get_db,Base,engine
from Database.commit_to_db import commit_data_on_db

def main():
    Status = ['CONFIRMED','PAID','OWNER','UNAVAILABLE','UNPAID']
    data = get_bookings_description(date_begin="2024-01-01",date_end="2024-12-01",status=Status)
    Base.metadata.create_all(engine)
    commit_data_on_db(bookings=data,db = get_db())

main()