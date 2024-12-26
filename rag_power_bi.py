import json
import requests
import msal
from powerbiclient import Report

from credentials import username, password

# Constants
TENANT_ID = '057866cb-0e0f-4818-bd4a-0255845df359'
CLIENT_ID = '04bb970d-3099-4845-b81d-92e23362f261'
CLIENT_SECRET = 'Tld8Q~hX_c4u8oYJfrdVd3KeZDvVVcpesAFywdce'
AUTHORITY_URL = f'https://login.microsoftonline.com/organizations'
SCOPE = ["https://api.fabric.microsoft.com/Dataset.ReadWrite.All",
    "https://api.fabric.microsoft.com/Dashboard.ReadWrite.All",
    "https://api.fabric.microsoft.com/Item.ReadWrite.All",
    "https://api.fabric.microsoft.com/Workspace.ReadWrite.All",
    "https://api.fabric.microsoft.com/Report.ReadWrite.All",
    "https://api.fabric.microsoft.com/Content.Create"]

GROUP_ID = 'ceb0d1d0-6226-4aef-b245-fac7f89bb52e'
POWER_BI_API_URL = f'https://api.powerbi.com/v1.0/myorg/'
REDIRECT_URI = 'http://localhost'

# Variables
access_token = ''

# Authenticate and get access token
if not access_token:
    app = msal.PublicClientApplication(
        CLIENT_ID,
        authority=AUTHORITY_URL
    )
    result = app.acquire_token_interactive(scopes=SCOPE)
    print(result)
    if 'access_token' in result:
        access_token = result['access_token']
    else:
        print(f'Error obtaining access token: {result}')

headers = {'Authorization': f'Bearer {access_token}'}

# Retrieve datasets
def get_datasets():
    response = requests.get(f'{POWER_BI_API_URL}datasets', headers=headers)
    if response.status_code == 200:
        # create a json file with the datasets in responses folder
        with open('responses/datasets.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
        return response.json()
    print(f'Error retrieving datasets: {response}')

# Retrieve reports
def get_reports(groupId):
    response = requests.get(f'{POWER_BI_API_URL}/groups/{groupId}/reports', headers=headers)
    if response.status_code == 200:
        # create a json file with the reports in responses folder
        with open('responses/reports.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
        return response.json()
    print(f'Error retrieving reports: {response}')

# Retrieve dashboards
def get_dashboards(groupId):
    response = requests.get(f'{POWER_BI_API_URL}/groups/{groupId}/dashboards', headers=headers)
    if response.status_code == 200:
        # create a json file with the dashboards in responses folder
        with open('responses/dashboards.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
        return response.json()
    print(f'Error retrieving dashboards: {response}')# Retrieve groups

def get_groups():
    response = requests.get(f'{POWER_BI_API_URL}groups', headers=headers)
    if response.status_code == 200:
        # create a json file with the groups in responses folder
        with open('responses/groups.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
        return response.json()
    else:
        print(f'Error retrieving groups: {response}')# Retrieve users

def get_users(groupId):
    response = requests.get(f'{POWER_BI_API_URL}/groups/{groupId}/users', headers=headers)
    if response.status_code == 200:
        # create a json file with the users in responses folder
        with open('responses/users.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
        return response.json()
    else:
        print(f'Error retrieving users: {response}')

def get_pages(groupId,report_id):
    response = requests.get(f'{POWER_BI_API_URL}/groups/{groupId}/reports/{report_id}/pages', headers=headers)
    if response.status_code == 200:
        with open(f'responses/pages_{report_id}.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
    else:
        print(f'Error retrieving pages: {response}')
    return response.json()

# Retrieve dataflow sources
# Summarize information
def summarize_info():
    datasets = get_datasets()
    reports = get_reports(GROUP_ID)
    dashboards = get_dashboards(GROUP_ID)
    groups = get_groups()
    users = get_users(GROUP_ID)

    summary = {
        'total_datasets': [dataset['name'] for dataset in datasets['value']] if datasets and 'value' in datasets else [],
        'total_reports': {report['name']: report['id'] for report in reports['value']} if reports and 'value' in reports else {},
        'total_dashboards': [dashboard['displayName'] for dashboard in dashboards['value']] if dashboards and 'value' in dashboards else [],
        'total_groups': [group['name'] for group in groups['value']] if groups and 'value' in groups else [],
        'total_users': [user['displayName'] for user in users['value']] if users and 'value' in users else [],
        # in 'pages' put a list of pages for each report
        'pages': {report['name']: get_pages(GROUP_ID, report['id'])["value"] for report in reports['value']} if reports and 'value' in reports else {}
        }
    with open('responses/summary.json', 'w') as f:
        f.write(json.dumps(summary, indent=4))
    return summary

# Main function
def main1():
    if access_token:
        get_pages(GROUP_ID,"025bdeaf-cf4e-40b9-a4c6-01446cbdff3f")
        # put summary in a json file
        with open('responses/summary.json', 'w') as f:
            f.write(json.dumps(summarize_info(), indent=4))


def get_active_page(report: Report):
    pages = report.get_pages()
    active_page = {}
    for page in pages:
        if page['isActive'] == True:
            active_page = page
            break
        return active_page

def loaded_callback(event_details):
    print('Report is loaded')

def rendered_callback(event_details):
    print('Report is rendered')


def main2():
    if access_token:
        info = summarize_info()
        for report_id in info['total_reports'].values():
            #get report with access token in the future
            report = Report(group_id=GROUP_ID, report_id=report_id)

            #on function to render & load report
            report.on('loaded', loaded_callback)
            report.on('rendered', rendered_callback)

            active_page = get_active_page(report)
            active_page_name = active_page['name']
            visuals = report.visuals_on_page(active_page_name)
            for visual in visuals:
                summarized_exported_data = report.export_visual_data(active_page_name,
                                                                 visual['name'], rows=20)
                print(summarized_exported_data)
        #powerbi.Report().export_visual_data("7c653908f5a8a0f72bb0",)


if __name__ == '__main__':
    main2()