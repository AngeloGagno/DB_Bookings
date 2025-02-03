from API_Data.request_api import RequestBookingsAPI
from API_Data.bookings_description import Booking
from API_Data.get_bookings_id import create_booking_list,bookings_update

def get_bookings_description(date_begin=None,date_end=None,status=None):
    
    id_list = create_booking_list(date_begin=date_begin,date_end=date_end,status=status)
    bookings = []
    for id in id_list:
        data = RequestBookingsAPI().get_api_booking_description(booking_id=id)
        caract = Booking(data)
        booking = {'id_booking':id,'Portal Reference':caract.reference(),'check_in_date':caract.check_in_date(),
                   'check_out_date':caract.check_out_date(),
                   'update_date':caract.update_date(),
                   'reservation_date':caract.creation_date(),
                    'status':caract.status(), 'accommodation_code':caract.accommodation(),
                    'sale_channel':caract.sales_channel(),'total_payment':caract.total_payment(), 'net_payment':caract.net_payment(),
                    'extras_value': caract.extras_value(),'extra_info':str(caract.extra_info()), 'portal_comission':str(caract.portal_comission())}
        bookings.append(booking)
    return bookings

def get_booking_updates():
    id_list = bookings_update()
    bookings = []
    for id in id_list:
        data = RequestBookingsAPI().get_api_booking_description(booking_id=id)
        caract = Booking(data)
        booking = {'id_booking':id,'Portal Reference':caract.reference(),'check_in_date':caract.check_in_date(),
                   'check_out_date':caract.check_out_date(),'update_date':caract.update_date(),
                   'reservation_date':caract.creation_date(),
                    'status':caract.status(), 'accommodation_code':caract.accommodation(),
                    'sale_channel':caract.sales_channel(),'total_payment':caract.total_payment(), 'net_payment':caract.net_payment(),
                    'extras_value': caract.extras_value(),'extra_info':str(caract.extra_info()), 'portal_comission':str(caract.portal_comission())}
        bookings.append(booking)
    return bookings    
