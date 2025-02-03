import os
import requests
from dotenv import load_dotenv

class RequestBookingsAPI:
    def __init__(self, date_begin=None, date_end=None, statuses=None):
        """
        Inicializa a classe RequestBookingsAPI.
        Args:
            date_begin (str, opcional): Data de início no formato %Y-%m-%d.
            date_end (str, opcional): Data de término no formato %Y-%m-%d.
            statuses (list, opcional): Lista de status para filtrar.
        """
        self.date_begin = date_begin
        self.date_end = date_end
        self.statuses = statuses if statuses is not None else []
        self.apikey = self._apikey()
        self.header = self._header()
        self.raw_bookings_url = self._raw_bookings_url()
        self.final_url = self.get_booking_url()
        self.update_url = self.get_update_url()
        
    def _apikey(self):
        """
        Le a variavel de ambiente que contem a API Key: API_AVANTIO
        """
        load_dotenv(override=True)
        return os.getenv('API_AVANTIO')

    def _header(self):
        """
        Retorna o Header da API com a API key
        
        """
        return {
            "accept": "application/json",
            "X-Avantio-Auth": self.apikey
        }

    def _raw_bookings_url(self):
        return 'https://api.avantio.pro/pms/v2/bookings'

    def _filter_by_status(self):
        """
        Cria o filtro de status para a URL.
        """
        if not self.statuses:
            return ''
        statuses_query = "&status=".join(self.statuses)
        return f"&status={statuses_query}"

    def _filter_by_date(self):
        """
        Cria o filtro de datas para a URL.
        """
        if not self.date_begin and not self.date_end:
            return ''
        if not self.date_begin:
            return f"&creationDate_to={self.date_end}"
        if not self.date_end:
            return f"&creationDate_from={self.date_begin}"
        return f"&creationDate_from={self.date_begin}&creationDate_to={self.date_end}"

    def get_api_booking_description(self, booking_id):
        """
        Busca os detalhes de uma reserva específica.
        Args:
            booking_id (str): ID da reserva.
        """
        response = requests.get(f'{self.raw_bookings_url}/{booking_id}', headers=self.header)
        return response.json()

    def get_booking_url(self):
        """
        Gera a URL completa com filtros e retorna a lista de reservas.
        """
        url = self.raw_bookings_url    
        filters = '?pagination_size=50' + self._filter_by_date() + self._filter_by_status()
        url += filters
        return url
    
    def get_bookings_list(self,url_pag =None):
        """
        Gera a requisicao para a API das reservas criadas no determinado periodo
        """
        if url_pag:
            return requests.get(url_pag,headers=self.header).json()
        return requests.get(self.final_url,headers=self.header).json()

    def get_update_url(self):
        """
        Retorna a String para o booking updates
        """

        return 'https://api.avantio.pro/pms/v2/booking-updates?pagination_size=50'
    
    def get_bookings_update(self,url_pag =None):
        """
        Retorna as reservas alteradas sendo elas feitas ou com mudanca de status em um periodo de 24horas
        """
        if url_pag:
            return requests.get(url_pag,headers=self.header).json()
        return requests.get(self.update_url,headers=self.header).json()