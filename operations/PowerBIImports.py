import requests

class PowerBIImports:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://api.powerbi.com/v1.0/myorg/admin'

    @staticmethod
    def get_imports_as_admin(headers):
        url = f'{PowerBIImports.BASE_URL}/imports/getImportsAsAdmin?api-version={PowerBIImports.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()