import requests

class PowerBIInformationProtection:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://api.powerbi.com/v1.0/myorg/admin'

    @staticmethod
    def remove_labels_as_admin(headers, payload):
        url = f'{PowerBIInformationProtection.BASE_URL}/informationProtection/removeLabelsAsAdmin?api-version={PowerBIInformationProtection.API_VERSION}'
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    @staticmethod
    def set_labels_as_admin(headers, payload):
        url = f'{PowerBIInformationProtection.BASE_URL}/informationProtection/setLabelsAsAdmin?api-version={PowerBIInformationProtection.API_VERSION}'
        response = requests.post(url, json=payload, headers=headers)
        return response.json()