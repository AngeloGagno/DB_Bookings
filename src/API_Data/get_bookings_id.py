from API_Data.request_api import RequestBookingsAPI

def create_booking_list(date_begin=None,date_end=None, status:list = None):
    request = RequestBookingsAPI(date_begin=date_begin,date_end=date_end,statuses=status)
    url_request = request.get_booking_url()
    id_list = []
    while url_request:
        data = RequestBookingsAPI().get_bookings_list(url_request)
        id_list.extend(i['id'] for i in data['data'])
        url_request = data.get('_links', {}).get('next')  
        
    return id_list

def bookings_update():
    '''Recebe todos as reservas que entraram em um periodo de 24horas e que tiveram atualizacoes nesse mesmo periodo'''
    url_request = RequestBookingsAPI().get_update_url()
    id_list = []
    while url_request:
        data = RequestBookingsAPI().get_bookings_update(url_request)
        print(url_request)
        id_list.extend(i['id'] for i in data['data'])
        url_request = data.get('_links', {}).get('next')     
    return id_list 
if __name__ == "__main__":
    Status = ['CONFIRMED','PAID','OWNER','UNAVAILABLE','UNPAID']
    print(len(create_booking_list(date_begin="2024-01-01",date_end="2024-01-31",status=Status)))
        