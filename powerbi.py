import json
import pandas as pd
import requests
import msal
import papermill as pm
from io import StringIO
from powerbiclient import Report, models
from powerbiclient.authentication import DeviceCodeLoginAuthentication

from credentials import AUTHORITY_URL, CLIENT_ID, SCOPE, GROUP_ID, POWER_BI_API_URL, TENANT_ID

# Variables
access_token = ''

# Authenticate and get access token
if not access_token:
    app = msal.PublicClientApplication(
        CLIENT_ID,
        authority=AUTHORITY_URL
    )
    result = app.acquire_token_interactive(scopes=SCOPE)
    if 'access_token' in result:
        access_token = result['access_token']
        print('Access token obtained successfully by interactive login')
    else:
        print(f'Error obtaining access token: {result}, trying username and password')
        app = msal.PublicClientApplication(CLIENT_ID, authority=TENANT_ID)
        username = input('Enter username: ')
        password = input('Enter password: ')
        result = app.acquire_token_by_username_password(username, password, SCOPE)
        if 'access_token' in result:
            access_token = result['access_token']
            print('Access token obtained successfully by username and password')
        else:
            print(f'Error obtaining access token: {result}')

# Headers
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
    print(f'Error retrieving dashboards: {response}')  # Retrieve groups

def get_groups():
    response = requests.get(f'{POWER_BI_API_URL}groups', headers=headers)
    if response.status_code == 200:
        # create a json file with the groups in responses folder
        with open('responses/groups.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
        return response.json()
    else:
        print(f'Error retrieving groups: {response}')  # Retrieve users

def get_users(groupId):
    response = requests.get(f'{POWER_BI_API_URL}/groups/{groupId}/users', headers=headers)
    if response.status_code == 200:
        # create a json file with the users in responses folder
        with open('responses/users.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
        return response.json()
    else:
        print(f'Error retrieving users: {response}')

def get_pages(groupId, report_id):
    response = requests.get(f'{POWER_BI_API_URL}/groups/{groupId}/reports/{report_id}/pages', headers=headers)
    if response.status_code == 200:
        with open(f'responses/pages_{report_id}.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
    else:
        print(f'Error retrieving pages: {response}')
    return response.json()

def get_embed_token(groupId, report_id):
    request_body = {
        "accessLevel": "View",
        "allowSaveAs": "true"
    }
    headers.update({'Content-Type': 'application/json'})
    response = requests.post(f'{POWER_BI_API_URL}/groups/{groupId}/reports/{report_id}/GenerateToken', headers=headers, json=request_body)
    if response.status_code == 200:
        with open(f'responses/embed_token_{report_id}.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
    else:
        print(f'Error retrieving embed token: {response}')
    return response.json()['token']

def embed_report(report):
    def loaded_callback(event_details):
        print('Report is loaded')
    report.on('loaded', loaded_callback)
    def rendered_callback(event_details):
        print('Report is rendered')

    report.on('rendered', rendered_callback)
    report._embedded = True

# Summarize information
def summarize_info():
    # datasets = get_datasets()
    # dashboards = get_dashboards(GROUP_ID)
    # groups = get_groups()
    # users = get_users(GROUP_ID)
    reports = get_reports(GROUP_ID)

    summary = {}
    for report in reports['value']:
        summary[report['id']] = {
            'name': report['name'],
            'pages': get_pages(GROUP_ID, report['id'])['value'],
            'embed_token': get_embed_token(GROUP_ID, report['id']),
            'embed_url': report['embedUrl'],
            'dataset_id': report['datasetId'],
            'csv_files': []
        }

    # summary = {
    #     'total_datasets': [dataset['name'] for dataset in
    #                        datasets['value']] if datasets and 'value' in datasets else [],
    #
    #     # to-do change key - id / value - info
    #     'total_reports': {report['name']: report['id']} for report in
    #                       reports['value']} if reports and 'value' in reports else {},
    #     'total_dashboards': [dashboard['displayName'] for dashboard in
    #                          dashboards['value']] if dashboards and 'value' in dashboards else [],
    #     'total_groups': [group['name'] for group in groups['value']] if groups and 'value' in groups else [],
    #     'total_users': [user['displayName'] for user in users['value']] if users and 'value' in users else [],
    #     # in 'pages' put a list of pages for each report
    #     'pages': {report['name']: get_pages(GROUP_ID, report['id'])["value"] for report in
    #               reports['value']} if reports and 'value' in reports else {}
    # }

    with open('responses/summary.json', 'w') as f:
        f.write(json.dumps(summary, indent=4))
    return summary

def summarize_vis_info(report, pages):
    # Define the types of visuals to export data for
    visual_types_to_export = ['barChart', 'lineChart', 'pieChart', 'clusteredColumnChart', 'table', 'tableEx', 'map',
                              'slicer', 'lineClusteredColumnComboChart', 'shapeMap', 'decompositionTreeVisual', 'card']

    # Iterate over the visuals and export data for the specified types
    for page in pages:
        page_name = page['name']
        report.set_active_page(page_name)
        page_display_name = page['displayName']
        visuals = report.visuals_on_page(page_name)
        for visual in visuals:
            if visual['type'] in visual_types_to_export:
                try:
                    summarized_exported_data = report.export_visual_data(page_name, visual['name'], rows=20)
                    data = StringIO(summarized_exported_data)
                    # Load data into pandas DataFrame
                    df = pd.read_csv(data, sep=",")
                    # Store the DataFrame as a CSV file in the 'csv' folder
                    csv_file_path = f'csv/{visual["type"]}_{visual["title"].replace(" ", "_")}_{visual['name']}_{page_display_name.replace(" ", "_")}.csv'
                    df.to_csv(csv_file_path, index=False)
                    print(
                        f"Data for visual '{visual["title"].replace(" ", "")}' of type '{visual['type']}' exported successfully.")
                    return csv_file_path
                except Exception as e:
                    print(
                        f"Could not export data for visual '{visual["title"].replace(" ", "")}' of type '{visual['type']}': {e}")
        page['isActive'] = False

def main2():
    if access_token:
        info = summarize_info()
        for report_id in info.keys():
            print(f'Processing report: {info[report_id]["name"]}')
            #Get report and create Report class
            report = Report(group_id=GROUP_ID, report_id=report_id, auth=access_token)

            #Load, render and embed report
            report._set_embed_config(access_token=info[report_id]['embed_token'],
                                     embed_url=info[report_id]['embed_url'],
                                     view_mode=1,
                                     permissions=models.Permissions.ALL.value,
                                     dataset_id=info[report_id]['dataset_id'])
            embed_report(report)

            #Get visuals for all pages
            #info[report_id]['csv_files'].append(summarize_vis_info(report, report.get_pages()))

def main():
    if access_token:
        auth = DeviceCodeLoginAuthentication()
        info = summarize_info()
        for report_id in info['total_reports'].values():
            # Run Jupyter notebook powerbi_rag.ipynb with the specified report_id
            pm.execute_notebook(
                'powerbi_rag.ipynb',
                'powerbi_rag_output.ipynb',
                parameters=dict(report_id=report_id, auth=auth)
            )

if __name__ == '__main__':
    main2()

