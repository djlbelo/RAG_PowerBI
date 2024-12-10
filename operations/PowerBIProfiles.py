import requests


class PowerBIProfiles:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://api.powerbi.com/v1.0/myorg/admin'

    @staticmethod
    def delete_profile_as_admin(headers, payload):
        url = f'{PowerBIProfiles.BASE_URL}/profiles/deleteProfileAsAdmin?api-version={PowerBIProfiles.API_VERSION}'
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    @staticmethod
    def get_profiles_as_admin(headers):
        url = f'{PowerBIProfiles.BASE_URL}/profiles/getProfilesAsAdmin?api-version={PowerBIProfiles.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()