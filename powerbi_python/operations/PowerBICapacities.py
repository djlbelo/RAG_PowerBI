import requests


class PowerBICapacities:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://api.powerbi.com/v1.0/myorg/admin'

    @staticmethod
    def assign_workspaces_to_capacity(headers, payload):
        url = f'{PowerBICapacities.BASE_URL}/capacities/assignWorkspacesToCapacity?api-version={PowerBICapacities.API_VERSION}'
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    @staticmethod
    def get_capacity_users_as_admin(headers):
        url = f'{PowerBICapacities.BASE_URL}/capacities/getCapacityUsersAsAdmin?api-version={PowerBICapacities.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def unassign_workspaces_from_capacity(headers, payload):
        url = f'{PowerBICapacities.BASE_URL}/capacities/unassignWorkspacesFromCapacity?api-version={PowerBICapacities.API_VERSION}'
        response = requests.post(url, json=payload, headers=headers)
        return response.json()