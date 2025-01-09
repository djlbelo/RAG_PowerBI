import requests

class PowerBIDashboards:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://api.powerbi.com/v1.0/myorg/admin'

    @staticmethod
    def get_dashboard_subscriptions_as_admin(headers):
        url = f'{PowerBIDashboards.BASE_URL}/dashboards/getDashboardSubscriptionsAsAdmin?api-version={PowerBIDashboards.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_dashboard_users_as_admin(headers):
        url = f'{PowerBIDashboards.BASE_URL}/dashboards/getDashboardUsersAsAdmin?api-version={PowerBIDashboards.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_dashboards_as_admin(headers):
        url = f'{PowerBIDashboards.BASE_URL}/dashboards/getDashboardsAsAdmin?api-version={PowerBIDashboards.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_dashboards_in_group_as_admin(group_id, headers):
        url = f'{PowerBIDashboards.BASE_URL}/groups/{group_id}/dashboards/getDashboardsInGroupAsAdmin?api-version={PowerBIDashboards.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_tiles_as_admin(headers):
        url = f'{PowerBIDashboards.BASE_URL}/dashboards/getTilesAsAdmin?api-version={PowerBIDashboards.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()