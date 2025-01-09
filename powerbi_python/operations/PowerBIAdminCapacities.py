import requests

class PowerBIAdminCapacities:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://api.powerbi.com/v1.0/myorg/admin'

    @staticmethod
    def get_capacities_as_admin(headers):
        url = f'{PowerBIAdminCapacities.BASE_URL}/capacities/getCapacitiesAsAdmin?api-version={PowerBIAdminCapacities.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()