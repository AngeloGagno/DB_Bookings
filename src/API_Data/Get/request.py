import requests
from dotenv import load_dotenv
import os 


class Request_Bookings_API:
    def __init__(self,date_begin=None,date_end=None):
        self.apikey = self._apikey()    
        self.header = self.header()
        self.checkin_begin = date_begin
        self.checkin_ends = date_end
    def _apikey(self):
        load_dotenv()
        api = os.getenv('API_AVANTIO')
        return api

    def header(self):
        return {
        "accept": "application/json",
        "X-Avantio-Auth": self.apikey
    }

    def get_api_response(self):
        status = requests.get('https://api.avantio.pro/pms/v2/bookings',headers=self.header)
        return status.status_code
    
    def get_api_data(self):
        return requests.get(fr'https://api.avantio.pro/pms/v2/bookings?arrivalDate_from={self.checkin_begin}&arrivalDate_to={self.checkin_ends}',headers = self.header).json()

api = Request_Bookings_API('2024-12-01','2024-12-02')
print(api.get_api_data())