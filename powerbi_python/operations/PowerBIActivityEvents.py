import requests


class PowerBIActivityEvents:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://api.powerbi.com/v1.0/myorg/admin'

    @staticmethod
    def get_activity_events(headers):
        url = f'{PowerBIActivityEvents.BASE_URL}/activityEvents/getActivityEvents?api-version={PowerBIActivityEvents.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()