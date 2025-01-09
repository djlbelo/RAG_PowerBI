import requests

class PowerBIOverview:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://management.azure.com/subscriptions/{subscriptionId}/providers/Microsoft.PowerBIDedicated'

    @staticmethod
    def add_power_bi_encryption_key(subscription_id, headers, payload):
        url = f'{PowerBIOverview.BASE_URL}/encryptionKeys?api-version={PowerBIOverview.API_VERSION}'
        response = requests.post(url.format(subscriptionId=subscription_id), json=payload, headers=headers)
        return response.json()

    @staticmethod
    def get_power_bi_encryption_keys(subscription_id, headers):
        url = f'{PowerBIOverview.BASE_URL}/encryptionKeys?api-version={PowerBIOverview.API_VERSION}'
        response = requests.get(url.format(subscriptionId=subscription_id), headers=headers)
        return response.json()

    @staticmethod
    def rotate_power_bi_encryption_key(subscription_id, headers, payload):
        url = f'{PowerBIOverview.BASE_URL}/encryptionKeys/rotate?api-version={PowerBIOverview.API_VERSION}'
        response = requests.post(url.format(subscriptionId=subscription_id), json=payload, headers=headers)
        return response.json()