import requests, json, msal

from credentials import AUTHORITY_URL, CLIENT_ID, SCOPE, GROUP_ID, POWER_BI_API_URL, TENANT_ID

access_token = ''

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

        app = msal.PublicClientApplication(
            CLIENT_ID,
            authority=TENANT_ID
        )
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

# Summarize information
def summarize_info():
    summary = {}
    for group in get_groups()['value']:
        group_id = group['id']
        summary[group_id] = {}
        for report in get_reports(group_id)['value']:
            summary[group_id][report['id']] = {
                'name': report['name'],
                'pages': get_pages(GROUP_ID, report['id'])['value'],
                'embed_token': get_embed_token(GROUP_ID, report['id']),
                'embed_url': report['embedUrl'],
                'dataset_id': report['datasetId'],
                'csv_files': []
            }

    with open('responses/summary.json', 'w') as f:
        f.write(json.dumps(summary, indent=4))
    return summary

summarize_info()