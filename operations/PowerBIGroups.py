import requests

class PowerBIGroups:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://api.powerbi.com/v1.0/myorg/admin'

    @staticmethod
    def add_user_as_admin(headers, payload):
        url = f'{PowerBIGroups.BASE_URL}/groups/addUserAsAdmin?api-version={PowerBIGroups.API_VERSION}'
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    @staticmethod
    def delete_user_as_admin(headers, payload):
        url = f'{PowerBIGroups.BASE_URL}/groups/deleteUserAsAdmin?api-version={PowerBIGroups.API_VERSION}'
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    @staticmethod
    def get_group_as_admin(headers):
        url = f'{PowerBIGroups.BASE_URL}/groups/getGroupAsAdmin?api-version={PowerBIGroups.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_group_users_as_admin(headers):
        url = f'{PowerBIGroups.BASE_URL}/groups/getGroupUsersAsAdmin?api-version={PowerBIGroups.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_groups_as_admin(headers):
        url = f'{PowerBIGroups.BASE_URL}/groups/getGroupsAsAdmin?api-version={PowerBIGroups.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_unused_artifacts_as_admin(headers):
        url = f'{PowerBIGroups.BASE_URL}/groups/getUnusedArtifactsAsAdmin?api-version={PowerBIGroups.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def restore_deleted_group_as_admin(headers, payload):
        url = f'{PowerBIGroups.BASE_URL}/groups/restoreDeletedGroupAsAdmin?api-version={PowerBIGroups.API_VERSION}'
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    @staticmethod
    def update_group_as_admin(headers, payload):
        url = f'{PowerBIGroups.BASE_URL}/groups/updateGroupAsAdmin?api-version={PowerBIGroups.API_VERSION}'
        response = requests.patch(url, json=payload, headers=headers)
        return response.json()