import requests

class PowerBIRefreshables:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://api.powerbi.com/v1.0/myorg/admin'

    @staticmethod
    def get_refreshable_for_capacity(headers):
        url = f'{PowerBIRefreshables.BASE_URL}/refreshables/getRefreshableForCapacity?api-version={PowerBIRefreshables.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_refreshables(headers):
        url = f'{PowerBIRefreshables.BASE_URL}/refreshables/getRefreshables?api-version={PowerBIRefreshables.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_refreshables_for_capacity(headers):
        url = f'{PowerBIRefreshables.BASE_URL}/refreshables/getRefreshablesForCapacity?api-version={PowerBIRefreshables.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()