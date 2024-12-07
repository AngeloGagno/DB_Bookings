
from request import Request_Bookings_API

class Booking:
    def __init__(self,data):
        self.data = data['data']
        self.payments = data['data']['amounts']
        
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
    
    def sales_channel(self):
        return self.data.get('salesChannel',{}).get('name','')
    
    def net_payment(self):
        return self.payments['breakdown']['base']['net']

    def tourism_tax(self):
        return self.payments.get('taxes',{}).get('tourism',{}).get('net',0)
    
    def portal_comission(self):
        return self.payments['commission']['portal']

data = Request_Bookings_API().get_api_booking_description('23322808') 
print(Booking(data).check_out_date())

