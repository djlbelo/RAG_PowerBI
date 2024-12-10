import requests

class PowerBIApps:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://api.powerbi.com/v1.0/myorg/admin'

    @staticmethod
    def get_app_users_as_admin(headers):
        url = f'{PowerBIApps.BASE_URL}/apps/getAppUsersAsAdmin?api-version={PowerBIApps.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_apps_as_admin(headers):
        url = f'{PowerBIApps.BASE_URL}/apps/getAppsAsAdmin?api-version={PowerBIApps.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()