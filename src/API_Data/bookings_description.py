
class Booking:
    def __init__(self,data):
        self.data = data['data']
        self.payments = data['data']['amounts']

    def reference(self):
        return self.data['reference']
    
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
    
    def total_payment(self):
        return self.payments.get('total',{}).get('net',0)/1000
    
    def extra_info(self):
        if len(self.data['extras']) == 0:
            return self.data['extras']
        else:
            result = [
    {'reference': item['info']['reference'], 'net_price': item['price']['net']/1000}
        for item in self.data['extras'] if item['price']['net'] > 0]   
            return result
    
    def net_payment(self):
        return self.payments['breakdown']['base']['net']/1000

    def extras_value(self):
        return self.payments['breakdown'].get('extras',{}).get('net',0)/1000
    
    def portal_comission(self):
        return self.payments['commission']['portal']/1000


