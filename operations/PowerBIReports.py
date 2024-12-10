import requests


class PowerBIReports:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://api.powerbi.com/v1.0/myorg/admin'

    @staticmethod
    def get_report_subscriptions_as_admin(headers):
        url = f'{PowerBIReports.BASE_URL}/reports/getReportSubscriptionsAsAdmin?api-version={PowerBIReports.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_report_users_as_admin(headers):
        url = f'{PowerBIReports.BASE_URL}/reports/getReportUsersAsAdmin?api-version={PowerBIReports.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_reports_as_admin(headers):
        url = f'{PowerBIReports.BASE_URL}/reports/getReportsAsAdmin?api-version={PowerBIReports.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_reports_in_group_as_admin(group_id, headers):
        url = f'{PowerBIReports.BASE_URL}/groups/{group_id}/reports/getReportsInGroupAsAdmin?api-version={PowerBIReports.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()