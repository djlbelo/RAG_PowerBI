import requests


class PowerBIUsers:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://api.powerbi.com/v1.0/myorg/admin'

    @staticmethod
    def get_user_artifact_access_as_admin(headers):
        url = f'{PowerBIUsers.BASE_URL}/users/getUserArtifactAccessAsAdmin?api-version={PowerBIUsers.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_user_subscriptions_as_admin(headers):
        url = f'{PowerBIUsers.BASE_URL}/users/getUserSubscriptionsAsAdmin?api-version={PowerBIUsers.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()