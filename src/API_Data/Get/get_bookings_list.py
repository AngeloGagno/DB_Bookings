
from request import Request_Bookings_API

class Booking:
    def __init__(self,data):
        self.data = data['data']

    def check_in_date(self):
        return self.data['stayDates']['arrival']

    def check_out_date(self):
        return self.data['stayDates']['departure']
    
    def creation_date(self):
        return self.data['creationDate']

    def status(self):
        return self.data['status']
    
    def accommodation(self):
        return self.data['accommodation']['id']
    
data = Request_Bookings_API().get_api_booking_description('23895641') 
print(Booking(data).creation_date())

