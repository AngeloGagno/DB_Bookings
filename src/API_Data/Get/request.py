import requests
from dotenv import load_dotenv
import os 


class Request_Bookings_API:

    def __init__(self):
        self.apikey = self._apikey()    
        self.header = self._header()

    def _apikey(self):
        load_dotenv()
        api = os.getenv('API_AVANTIO')
        return api

    def _header(self):
        return {
        "accept": "application/json",
        "X-Avantio-Auth": self.apikey
    }

    def _get_api_booking_list(self):
        status = requests.get('https://api.avantio.pro/pms/v2/bookings',headers=self.header)
        return status.status_code
    
    def _get_api_booking_description(self):
        status = requests.get('https://api.avantio.pro/pms/v2/bookings',headers=self.header)
        return status.status_code
    
    def get_api_booking_description(self,id):
        '''
        id - Booking ID
        '''
        return requests.get(f'https://api.avantio.pro/pms/v2/bookings/{id}',headers=self.header).json()
        
    
    def get_bookings_list(self,checkin_begin:str,checkin_ends:str):
        '''
        date_begin and date_end - Must be a string format(%Y-%m-%d) \n
        %Y - Year \n
        %m - Month \n
        %d - Day 
        '''     
        return requests.get(fr'https://api.avantio.pro/pms/v2/bookings?arrivalDate_from={checkin_begin}&arrivalDate_to={checkin_ends}',headers = self.header).json()
