import requests

class PowerBIDatasets:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://api.powerbi.com/v1.0/myorg/admin'

    @staticmethod
    def get_dataset_to_dataflows_links_in_group_as_admin(group_id, headers):
        url = f'{PowerBIDatasets.BASE_URL}/groups/{group_id}/datasets/getDatasetToDataflowsLinksInGroupAsAdmin?api-version={PowerBIDatasets.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_dataset_users_as_admin(headers):
        url = f'{PowerBIDatasets.BASE_URL}/datasets/getDatasetUsersAsAdmin?api-version={PowerBIDatasets.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_datasets_as_admin(headers):
        url = f'{PowerBIDatasets.BASE_URL}/datasets/getDatasetsAsAdmin?api-version={PowerBIDatasets.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_datasets_in_group_as_admin(group_id, headers):
        url = f'{PowerBIDatasets.BASE_URL}/groups/{group_id}/datasets/getDatasetsInGroupAsAdmin?api-version={PowerBIDatasets.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_datasources_as_admin(headers):
        url = f'{PowerBIDatasets.BASE_URL}/datasets/getDatasourcesAsAdmin?api-version={PowerBIDatasets.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()