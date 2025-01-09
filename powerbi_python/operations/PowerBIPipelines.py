import requests

class PowerBIPipelines:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://api.powerbi.com/v1.0/myorg/admin'

    @staticmethod
    def delete_user_as_admin(headers, payload):
        url = f'{PowerBIPipelines.BASE_URL}/pipelines/deleteUserAsAdmin?api-version={PowerBIPipelines.API_VERSION}'
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    @staticmethod
    def get_pipeline_users_as_admin(headers):
        url = f'{PowerBIPipelines.BASE_URL}/pipelines/getPipelineUsersAsAdmin?api-version={PowerBIPipelines.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_pipelines_as_admin(headers):
        url = f'{PowerBIPipelines.BASE_URL}/pipelines/getPipelinesAsAdmin?api-version={PowerBIPipelines.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def update_user_as_admin(headers, payload):
        url = f'{PowerBIPipelines.BASE_URL}/pipelines/updateUserAsAdmin?api-version={PowerBIPipelines.API_VERSION}'
        response = requests.patch(url, json=payload, headers=headers)
        return response.json()