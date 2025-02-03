from sqlalchemy import Column, String, Float
from Database.database import Base

class BD_Bookings(Base):
    __tablename__ = 'bookings_1'
    id_booking = Column(String,primary_key=True)
    portal_reference = Column(String)
    check_in_data = Column(String)
    check_out_data = Column(String)
    update_date = Column(String)
    reservation_date = Column(String)
    status = Column(String)
    accommodation_code = Column(String)
    sale_channel = Column(String)
    total_payment = Column(Float)
    net_payment = Column(Float)
    extra_value = Column(Float)
    extra_descrition = Column(String)
    portal_comission = Column(Float)
