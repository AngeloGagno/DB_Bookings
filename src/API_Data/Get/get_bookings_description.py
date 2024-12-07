from API_Data.Get.request_api import RequestBookingsAPI
from API_Data.Get.bookings_description import Booking
from API_Data.Get.get_bookings_id import create_booking_list
import pandas as pd

def get_bookings_description(date_begin,date_end,status):
    
    id_list = create_booking_list(date_begin=date_begin,date_end=date_end,status=status)
    bookings = []
    for id in id_list:
        data = RequestBookingsAPI().get_api_booking_description(booking_id=id)
        caract = Booking(data)
        booking = {'id_booking':id,'Portal Reference':caract.reference(),'check_in_date':caract.check_in_date(),#colocar como datetime python
                   'check_out_date':caract.check_out_date(),#colocar como datetime python
                   'reservation_date':caract.creation_date(),#colocar como datetime python
                    'status':caract.status(), 'accommodation_code':caract.accommodation(),
                    'sale_channel':caract.sales_channel(),'total_payment':caract.total_payment(), 'net_payment':caract.net_payment(),
                    'extras_value': caract.extras_value(),'extra_info':str(caract.extra_info()), 'portal_comission':str(caract.portal_comission())}
        bookings.append(booking)
    return bookings
        
if __name__ == '__main__':
    Status = ['CONFIRMED','PAID','OWNER','UNAVAILABLE','UNPAID']
    get_bookings_description(date_begin='2024-01-01',date_end='2024-01-02',status=Status).to_excel('teste.xlsx')