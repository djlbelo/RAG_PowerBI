import requests

class PowerBIDataflows:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://api.powerbi.com/v1.0/myorg/admin'

    @staticmethod
    def export_dataflow_as_admin(headers, payload):
        url = f'{PowerBIDataflows.BASE_URL}/dataflows/exportDataflowAsAdmin?api-version={PowerBIDataflows.API_VERSION}'
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    @staticmethod
    def get_dataflow_datasources_as_admin(headers):
        url = f'{PowerBIDataflows.BASE_URL}/dataflows/getDataflowDatasourcesAsAdmin?api-version={PowerBIDataflows.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_dataflow_users_as_admin(headers):
        url = f'{PowerBIDataflows.BASE_URL}/dataflows/getDataflowUsersAsAdmin?api-version={PowerBIDataflows.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_dataflows_as_admin(headers):
        url = f'{PowerBIDataflows.BASE_URL}/dataflows/getDataflowsAsAdmin?api-version={PowerBIDataflows.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_dataflows_in_group_as_admin(group_id, headers):
        url = f'{PowerBIDataflows.BASE_URL}/groups/{group_id}/dataflows/getDataflowsInGroupAsAdmin?api-version={PowerBIDataflows.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_upstream_dataflows_in_group_as_admin(group_id, headers):
        url = f'{PowerBIDataflows.BASE_URL}/groups/{group_id}/dataflows/getUpstreamDataflowsInGroupAsAdmin?api-version={PowerBIDataflows.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()